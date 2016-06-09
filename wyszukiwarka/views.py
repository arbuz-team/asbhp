# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.db.models import Q
import operator
from forms import *
from produkt.models import *


################## Wyszukiwarka ##################

def Wyszukaj(request):

    if request.method == 'POST':
        wyszukiwarka = Formularz_Wyszukiwarki(request.POST)
        request.session['wyszukiwarka'] = wyszukiwarka
        wynik = []

        if wyszukiwarka.is_valid():
            zapytanie = wyszukiwarka.cleaned_data['zapytanie'].split(' ')
            request.session['zapytanie'] = wyszukiwarka.cleaned_data['zapytanie']

            wynik_sql = Produkt.objects.filter(
                reduce(operator.or_, (Q(nazwa__icontains=s) for s in zapytanie))        |
                reduce(operator.or_, (Q(opis__icontains=s) for s in zapytanie))         |
                reduce(operator.or_, (Q(producent__nazwa__icontains=s) for s in zapytanie)) |
                reduce(operator.or_, (Q(kolor__nazwa__icontains=s) for s in zapytanie)) |
                reduce(operator.or_, (Q(rodzaj__nazwa__icontains=s) for s in zapytanie)) |
                reduce(operator.or_, (Q(rodzaj__dziedzina__nazwa__icontains=s) for s in zapytanie)) |
                reduce(operator.or_, (Q(rodzaj__dziedzina__typ__nazwa__icontains=s) for s in zapytanie))
            )

                # p - pojedynczy produkt
            wynik_str = [(index, (p.nazwa + p.opis + p.producent.nazwa +
                                 p.kolor.nazwa + p.rodzaj.nazwa).lower())
                         for index, p in enumerate(wynik_sql)]

                # tworzę listę krotek określających pozycje produktów
            pozycja = []
            for produkt in wynik_str:
                trafienia = 0
                for slowo in zapytanie:
                    trafienia += produkt[1].count(slowo.lower())
                pozycja.append((trafienia, produkt[0])) # (trafienia, id)

            pozycja.sort(reverse=True)

                # tworzę posortowaną listę produktów
            for produkt in pozycja:
                wynik.append(wynik_sql[produkt[1]]) # produkt[1], to index

    else:
        wynik = []

    request.session['wyszukane_produkty'] = wynik
    return redirect('Wyswietl_Oferta')


def Pobierz_Formularz_Wyszukiwarki(request):
    wyszukiwarka = Formularz_Wyszukiwarki()

    if 'zapytanie' in request.session:
        wyszukiwarka.Ustaw_Zapytanie(request.session['zapytanie'])

    return wyszukiwarka


def Usun_Sesje(request):

    if 'zapytanie' in request.session:
        del request.session['zapytanie']

    if 'wyszukane_produkty' in request.session:
        del request.session['wyszukane_produkty']

    if 'wyszukiwarka' in request.session:
        del request.session['wyszukiwarka']

    return redirect('Wyswietl_Oferta')


################## Filtry ##################

def Filtr_Producent(request):

    if request.method == 'POST':
        filtr = Formularz_Filtru_Producent(request.POST)

        if filtr.is_valid():

            if 'wyszukane_produkty' in request.session:
                request.session['wyszukane_produkty'] = \
                    request.session['wyszukane_produkty'].\
                        filter(producent=filtr.cleaned_data['producent'])

            else:
                request.session['wyszukane_produkty'] = \
                    Produkt.objects.filter(producent=filtr.cleaned_data['producent'])

    return redirect('Wyswietl_Oferta')


def Filtr_Kolor(request):

    if request.method == 'POST':
        filtr = Formularz_Filtru_Kolor(request.POST)

        if filtr.is_valid():

            if 'wyszukane_produkty' in request.session:
                request.session['wyszukane_produkty'] = \
                    request.session['wyszukane_produkty']. \
                        filter(kolor=filtr.cleaned_data['kolor'])

            else:
                request.session['wyszukane_produkty'] = \
                    Produkt.objects.filter(kolor=filtr.cleaned_data['kolor'])

    return redirect('Wyswietl_Oferta')


def Filtr_Zagrozenia(request):

    if request.method == 'POST':
        filtr = Formularz_Filtru_Zagrozenia(request.POST)

        if filtr.is_valid():

            if 'wyszukane_produkty' in request.session:
                request.session['wyszukane_produkty'] = \
                    request.session['wyszukane_produkty']. \
                        filter(zagrozenia=filtr.cleaned_data['zagrozenia'])

            else:
                request.session['wyszukane_produkty'] = \
                    Produkt.objects.filter(zagrozenia=filtr.cleaned_data['zagrozenia'])

    return redirect('Wyswietl_Oferta')


def Filtr_Zawody(request):

    if request.method == 'POST':
        filtr = Formularz_Filtru_Zawody(request.POST)

        if filtr.is_valid():

            if 'wyszukane_produkty' in request.session:
                request.session['wyszukane_produkty'] = \
                    request.session['wyszukane_produkty']. \
                        filter(zawody=filtr.cleaned_data['zawody'])

            else:
                request.session['wyszukane_produkty'] = \
                    Produkt.objects.filter(zawody=filtr.cleaned_data['zawody'])

    return redirect('Wyswietl_Oferta')


################## Kontenery ##################

def Kontener_Typ(request):

    if 'wybrany_dziedzina' in request.session:
        del request.session['wybrany_dziedzina']

    if 'wybrany_rodzaj' in request.session:
        del request.session['wybrany_rodzaj']

    if request.method == 'POST':
        kontener = Formularz_Kontener(request.POST)

        if kontener.is_valid():
            request.session['wybrany_typ'] = kontener.cleaned_data['zawartosc']

        else:
            del request.session['wybrany_typ']

    return redirect('Wyswietl_Oferta')


def Kontener_Dziedzina(request):

    if 'wybrany_rodzaj' in request.session:
        del request.session['wybrany_rodzaj']

    if request.method == 'POST':
        kontener = Formularz_Kontener(request.POST)

        if kontener.is_valid():
            request.session['wybrany_dziedzina'] = kontener.cleaned_data['zawartosc']

        else:
            del request.session['wybrany_dziedzina']

    return redirect('Wyswietl_Oferta')


def Kontener_Rodzaj(request):

    if request.method == 'POST':
        kontener = Formularz_Kontener(request.POST)

        if kontener.is_valid():
            request.session['wybrany_rodzaj'] = kontener.cleaned_data['zawartosc']

        else:
            del request.session['wybrany_rodzaj']

    return redirect('Wyswietl_Oferta')
