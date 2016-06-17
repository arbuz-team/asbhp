# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
import operator
from django.http import Http404
from django.contrib.auth.hashers import make_password

import komunikat
from wyszukiwarka.forms import *
from produkt.forms import *

################## Zarządzanie sesją ##################

def Sprawdz_Sesje(request):

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
    Sprawdz_Sesje(request)

    if not request.session['zalogowany']:
        komunikat = 'Nic tu nie znajdziesz. Idź poszukać gdzieś indziej ;).'
        raise Http404(komunikat)

    return None


################## Komunikaty ##################

