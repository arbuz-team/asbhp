# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.db.models import Q
import operator
from forms import *
from produkt.models import *

def Wyszukaj(request):

    if request.method == 'POST':
        wyszukiwarka = Formularz_Wyszukiwarki(request.POST)
        wynik = []

        if wyszukiwarka.is_valid():
            zapytanie = wyszukiwarka.cleaned_data['zapytanie'].split(' ')
            request.session['zapytanie'] = wyszukiwarka.cleaned_data['zapytanie']

            wynik_sql = Produkt.objects.filter(
                reduce(operator.or_, (Q(nazwa__icontains=s) for s in zapytanie))        |
                reduce(operator.or_, (Q(opis__icontains=s) for s in zapytanie))         |
                reduce(operator.or_, (Q(firma__nazwa__icontains=s) for s in zapytanie)) |
                reduce(operator.or_, (Q(kolor__nazwa__icontains=s) for s in zapytanie)) |
                reduce(operator.or_, (Q(rodzaj__nazwa__icontains=s) for s in zapytanie))
            )

                # p - pojedynczy produkt
            wynik_str = [(index, (p.nazwa + p.opis + p.firma.nazwa +
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

    if request.session.get('zapytanie', None):
        wyszukiwarka.Ustaw_Zapytanie(request.session['zapytanie'])

    return wyszukiwarka

def Usun_Sesje(request):

    if request.session.get('zapytanie', None):
        del request.session['zapytanie']

    if request.session.get('wyszukane_produkty', None):
        del request.session['wyszukane_produkty']

    return redirect('Wyswietl_Oferta')
