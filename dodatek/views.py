# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
import operator
from django.http import Http404
from django.contrib.auth.hashers import make_password

import komunikat
from wyszukiwarka.forms import *
from produkt.forms import *
from asbhp.models import *



################## Zarządzanie sesją ##################

def Sprawdz_Sesje(request, meta_tag=True):

        # WYWALIĆ PÓŹNIEJ - ZAWSZE ZALOGOWANY
    request.session['zalogowany'] = True

        # filtry
    if 'wyszukiwarka' not in request.session:
        request.session['wyszukiwarka'] = Formularz_Wyszukiwarki()

    if 'producent' not in request.session:
        request.session['producent'] = Formularz_Filtru_Producent()

    if 'kolor' not in request.session:
        request.session['kolor'] = Formularz_Filtru_Kolor()

    if 'zagrozenia' not in request.session:
        request.session['zagrozenia'] = Formularz_Filtru_Zagrozenia()

    if 'zawody' not in request.session:
        request.session['zawody'] = Formularz_Filtru_Zawody()

    if 'liczba_produktow' not in request.session:
        request.session['liczba_produktow'] = \
            Formularz_Filtru_Liczba_Produktow()

        # kontenery
    if 'typ' not in request.session:
        request.session['typ'] = Typ_Odziezy.objects.all()

    if 'dziedzina' not in request.session:
        request.session['dziedzina'] = []

    if 'rodzaj' not in request.session:
        request.session['rodzaj'] = []

        # wybrane kontenery
    if 'wybrany_typ' not in request.session:
        request.session['wybrany_typ'] = None

    if 'wybrany_dziedzina' not in request.session:
        request.session['wybrany_dziedzina'] = None

    if 'wybrany_rodzaj' not in request.session:
        request.session['wybrany_rodzaj'] = None

        # użytkownik
    if 'zalogowany' not in request.session:
        request.session['zalogowany'] = False

        # komunikaty
    if '404' not in request.session:
        request.session['404'] = 'Upss. Chyba się coś popsuło.'

        # email
    if 'wybrany_temat' not in request.session:
        request.session['wybrany_temat'] = ''

        # stopka_kontakt
    if 'stopka_kontakt' not in request.session:
        request.session['stopka_kontakt'] = \
            {'tytul': Zawartosc_Zakladki.objects.get(pk='/kontakt/').tytul,
             'tekst': Zawartosc_Zakladki.objects.get(pk='/kontakt/').tekst,}

        # meta tag
    if meta_tag:
        request.session['meta_tag'] = \
            Meta_Tagi.objects.get(pk=request.path)
    else: # opcja dla zakładek do edycji
        request.session['meta_tag'] = None

        # informuje skrypt JS, aby wyświetlił szczegóły
    request.session['wyswietl_szczegoly_produktu'] = 'false'
    if request.path.split('/')[1] == 'produkt':
        if request.path.split('/')[2].isdigit():
            request.session['wyswietl_szczegoly_produktu'] = 'true'

        # edycja zakładek 'o_firmie' 'kontakt'
    if 'formularz_o_firmie' not in request.session:
        request.session['formularz_o_firmie'] = None

    if 'formularz_kontakt' not in request.session:
        request.session['formularz_kontakt'] = None

        # formularz poczty
    if 'formularz_poczta' not in request.session:
        request.session['formularz_poczta'] = None




def Usun_Sesje_Wyszukiwarki(request):
    del request.session['wyszukiwarka']

    if 'wyszukane_produkty' in request.session:
        del request.session['wyszukane_produkty']

    return redirect('Wyswietl_Oferta')




def Usun_Sesje_Filtrow(request):
    Usun_Sesje_Wyszukiwarki(request)

    del request.session['producent']
    del request.session['kolor']
    del request.session['zagrozenia']
    del request.session['zawody']
    del request.session['liczba_produktow']
    del request.session['typ']
    del request.session['dziedzina']
    del request.session['rodzaj']
    del request.session['wybrany_typ']
    del request.session['wybrany_dziedzina']
    del request.session['wybrany_rodzaj']

    return redirect('Wyswietl_Oferta')




def Usun_Sesje_Poczty(request):
    del request.session['wybrany_temat']
    del request.session['formularz_poczta']
    return redirect('Wyswietl_Kontakt')




def Usun_Sesje(request):
    for klucz in request.session.keys():
        del request.session[klucz]




################## Funkcje dodatkowe ##################

def Iloczyn_Zbiorow(pierwszy_kolejnosc, drugi):
    iloczyn = []
    for w in pierwszy_kolejnosc:
        if w in drugi:
            iloczyn.append(w)

    return iloczyn




def Pobierz_Zawartosc_Strony(request, produkt, wybrana_strona):

    liczba = 8 # początkowa ilość stron

        # pobieram liczbę produktów na stronie
    if request.session['liczba_produktow'].is_valid():
        liczba = int(request.session['liczba_produktow']
                     .cleaned_data['liczba'])

        # podstawowe obliczenia
    liczba_stron = len(produkt) / float(liczba)
    wybrana_strona -= 1 # aby wyciągnąć prawidłową wartość z tablicy

        # dla pętli: [i * liczba: (i * liczba) + liczba]
    zawartosc_strony = produkt[wybrana_strona * liczba:
                        (wybrana_strona * liczba) + liczba]

        # zamieniam liczba_stron na integer
    if liczba_stron > int(liczba_stron):
        liczba_stron = int(liczba_stron) + 1

    return {'zawartosc_strony': zawartosc_strony,
            'liczba_stron':     int(liczba_stron)}




def Pobierz_Liste_Numerow_Stron(liczba_stron, wybrana_strona):

        # dla jednej strony zwraca pustą tablicę
    if liczba_stron < 2:
        return []

        # wyświetl wszystkie strony
    if liczba_stron <= 7:
        return range(1, liczba_stron + 1)

    else:
            # wyświetl: 1 2 3 4 5 ... n
        if wybrana_strona < 4: # ... - 0
            return range(1, 6) + [0, liczba_stron]

            # wyświetl: 1 ... n-4 n-3 n-2 n-1 n
        if wybrana_strona > liczba_stron - 3:
            return [1, 0] + range(liczba_stron - 4,
                                  liczba_stron + 1)

            # wyswietl: 1 ... a b c ... n
        return [1, 0, wybrana_strona - 1, wybrana_strona,
                wybrana_strona + 1, 0, liczba_stron]




################## Logowanie ##################

def Szyfruj(haslo):
    return make_password(password=haslo, salt='arbuz-team')




def Sprawdz_Czy_Zalogowany(request):
    Sprawdz_Sesje(request, False)

    if not request.session['zalogowany']:
        request.session['404'] = 'Nic tu nie znajdziesz. ' \
                                 'Idź poszukać gdzieś indziej ;). ' \
                                 'PS. Nie jesteś zalogowany.'

        raise Http404(request.session['404'])

    return None
