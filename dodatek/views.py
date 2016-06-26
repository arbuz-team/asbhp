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
            {'tytul': Kontakt.objects.get(przeznaczenie='tytul'),
             'tekst': Kontakt.objects.get(przeznaczenie='tekst')}

        # meta tag
    if meta_tag:
        request.session['meta_tag'] = \
            Meta_Tagi.objects.get(pk=request.path)
    else: # opcja dla zakładek do edycji
        request.session['meta_tag'] = None

        # wyświetlanie produktu
    request.session['wybrany_produkt'] = None


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


def Pobierz_Listy_Produktow(request, produkt):

    wynik = []
    liczba = 4

    if request.session['liczba_produktow'].is_valid():
        liczba = int(request.session['liczba_produktow']
                     .cleaned_data['liczba'])

        # tworzę listę zawierającą listy po określonej
        # ilości produktów w zmiennej liczba
    for i in range(0, (len(produkt) / liczba) + 1):
        wynik.append(produkt[i * liczba: (i * liczba) + liczba])

    return wynik


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
