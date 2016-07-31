# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
import operator, time
import unicodedata
from django.http import Http404
from django.contrib.auth.hashers import make_password
from functools import reduce
from collections import defaultdict

import komunikat
from wyszukiwarka.forms import *
import wyszukiwarka
from produkt.forms import *
from asbhp.forms import *



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

        # wybrane filtry
    if 'wybrany_filtr' not in request.session:
        request.session['wybrany_filtr'] = 1

                            # kontenery
    if 'typ' not in request.session:
        request.session['typ'] = []
            #Typ_Odziezy.objects.filter(nazwa__in=Produkt.objects.filter(
            #    producent__nazwa='Adler').values('rodzaj__dziedzina__typ__nazwa'))

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

    if 'wyszukane' not in request.session:
        request.session['wyszukane'] = \
            wyszukiwarka.views.Wyszukaj(request)

    if 'iloczyn' not in request.session:
        request.session['iloczyn'] = \
            Iloczyn_Zbiorow(request.session['wyszukane'],
                            wyszukiwarka.views.Konteneruj(request))

        # wyświetlane produkty na start
    if 'produkt' not in request.session:
        request.session['produkt'] = \
            Produkt.objects.filter(pk__in=Polecane.objects.all().
                                   values('produkt__pk'))

    if 'o_firmie' not in request.session:
        request.session['o_firmie'] = \
            Zawartosc_Zakladki.objects.get(pk='/o_firmie/')




def Usun_Sesje_Wyszukiwarki(request):

    del request.session['wyszukiwarka']
    del request.session['wyszukane']
    del request.session['iloczyn']
    del request.session['produkt']

    return redirect('Wyswietl_Oferta')




def Usun_Sesje_Kontenerow(request):

    request.session['typ'] = []
    request.session['dziedzina'] = []
    request.session['rodzaj'] = []
    request.session['wybrany_typ'] = None
    request.session['wybrany_dziedzina'] = None
    request.session['wybrany_rodzaj'] = None




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




def Usun_Sesje_Filtra(request, numer_filtra):

    if numer_filtra == '1':
        Usun_Sesje_Wyszukiwarki(request)

    if numer_filtra == '2':
        del request.session['producent']
        Usun_Sesje_Kontenerow(request)

    if numer_filtra == '3':
        del request.session['kolor']

    if numer_filtra == '4':
        del request.session['zagrozenia']

    if numer_filtra == '5':
        del request.session['zawody']

    if numer_filtra == '6':
        del request.session['liczba_produktow']

    if int(numer_filtra) in list(range(1, 6)):
        Sprawdz_Sesje(request, False)
        request.session['produkt'] = \
            Iloczyn_Zbiorow(wyszukiwarka.views.Filtruj(request),
                            wyszukiwarka.views.Konteneruj(request))

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

    kolejnosc = defaultdict(int) # słownik kolejności
    for numer, element in enumerate(list(pierwszy_kolejnosc)):
        kolejnosc[element] = numer

    iloczyn = set(pierwszy_kolejnosc) & set(drugi)
    iloczyn = sorted(iloczyn, key=lambda i: kolejnosc[i])
    iloczyn = list(iloczyn)

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
        return list(range(1, liczba_stron + 1))

    else:
            # wyświetl: 1 2 3 4 5 ... n
        if wybrana_strona < 4: # ... - 0
            return list(range(1, 6)) + [0, liczba_stron]

            # wyświetl: 1 ... n-4 n-3 n-2 n-1 n
        if wybrana_strona > liczba_stron - 3:
            return [1, 0] + list(range(liczba_stron - 4,
                                       liczba_stron + 1))

            # wyswietl: 1 ... a b c ... n
        return [1, 0, wybrana_strona - 1, wybrana_strona,
                wybrana_strona + 1, 0, liczba_stron]




def Konwertuj_Nazwe_Na_URL(nazwa):
    return nazwa.replace(' ', '_').lower()




def Usun_Polskie_Znaki(tekst):
    return unicodedata.normalize('NFKD', tekst)\
        .encode('ascii', 'ignore')




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
