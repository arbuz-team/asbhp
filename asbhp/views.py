# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
import operator
from forms import *

################## Zakładki ##################

def Start(request):
    polecane = Polecane.objects.all()
    return render(request, 'start.html', {'polecane': polecane})


def O_Firmie(request):
    css_menu = ['wybrany', '', '']
    return render(request, 'o_firmie.html', {'css_menu': css_menu})


def Oferta(request):
    css_menu = ['', 'wybrany', '']
    typ = Typ_Odziezy.objects.all()
    dziedzina = Dziedzina_Odziezy.objects.all()
    rodzaj = Rodzaj_Odziezy.objects.all()
    return render(request, 'oferta.html', {'css_menu': css_menu,
                                           'typ': typ,
                                           'dziedzina': dziedzina,
                                           'rodzaj': rodzaj})


def Kontakt(request):
    css_menu = ['', '', 'wybrany']
    return render(request, 'kontakt.html', {'css_menu': css_menu})


################## Opcje ##################

def Wyswietl_Produkt(request, pk):
    produkt = Produkt.objects.filter(id=pk).first()
    return render(request, 'produkt.html', {'produkt': produkt})


def Wyswietl_Polecane(request):
    polecane = Polecane.objects.all()
    return render(request, 'polecane.html', {'polecane': polecane})


def Wyszukaj(request):

    if request.method == 'POST':
        wyszukiwarka = Formularz_Wyszukiwarki(request.POST)
        wynik = []

        if wyszukiwarka.is_valid():
            zapytanie = wyszukiwarka.cleaned_data['zapytanie'].split(' ')
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
        wyszukiwarka = Formularz_Wyszukiwarki()
        wynik = []

    return render(request, 'wyszukaj.html', {'wyszukiwarka': wyszukiwarka,
                                             'wynik': wynik})


################## Dodawanie ##################

def Dodaj_Produkt(request):

    if request.method == 'POST':
        formularz = Formularz_Produktu(request.POST)

        if formularz.is_valid():
            produkt = formularz.save()
            return redirect('Wyswietl_Produkt', produkt.id)

    else:
        formularz = Formularz_Produktu()

    for f in formularz:
        if f.label not in ['Certyfikaty', 'Zagrozenia', 'Zawody']:
            f.label = ''

    return render(request, 'dodaj_produkt.html', {'formularz': formularz})


def Dodaj_Firma(request):

    if request.method == 'POST':
        formularz = Formularz_Firma(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Firma została poprawnie dodana.'
            return render(request, 'potwierdzenie.html', {'opis': opis})

    else:
        formularz = Formularz_Firma()

    return render(request, 'dodaj.html', {'formularz': formularz})


def Dodaj_Kolor(request):

    if request.method == 'POST':
        formularz = Formularz_Kolor(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Kolor został poprawnie dodany.'
            return render(request, 'potwierdzenie.html', {'opis': opis})

    else:
        formularz = Formularz_Kolor()

    return render(request, 'dodaj.html', {'formularz': formularz})


def Dodaj_Certyfikat(request):

    if request.method == 'POST':
        formularz = Formularz_Certyfikat(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Certyfikat został poprawnie dodany.'
            return render(request, 'potwierdzenie.html', {'opis': opis})

    else:
        formularz = Formularz_Certyfikat()

    return render(request, 'dodaj.html', {'formularz': formularz})


def Dodaj_Dodatek(request):

    if request.method == 'POST':
        formularz = Formularz_Dodatek(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Dodatek został poprawnie dodany.'
            return render(request, 'potwierdzenie.html', {'opis': opis})

    else:
        formularz = Formularz_Dodatek()

    return render(request, 'dodaj.html', {'formularz': formularz})


def Dodaj_Polecane(request):

    if request.method == 'POST':
        formularz = Formularz_Polecane(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Nowy produkt został poprawnie dodany do ' \
                   'listy produktów polecanych.'
            return render(request, 'potwierdzenie.html', {'opis': opis})

    else:
        formularz = Formularz_Polecane()

    return render(request, 'dodaj.html', {'formularz': formularz})


################## Usuwanie ##################

def Usun_Produkt(request, pk):
    Produkt.objects.get(id=pk).delete()
    return render(request, 'usun.html', {})


def Usun_Firma(request, pk):
    Firma.objects.get(id=pk).delete()
    return render(request, 'usun.html', {})


def Usun_Kolor(request, pk):
    Kolor.objects.get(id=pk).delete()
    return render(request, 'usun.html', {})


def Usun_Certyfikat(request, pk):
    Certyfikat.objects.get(id=pk).delete()
    return render(request, 'usun.html', {})


def Usun_Dodatek(request, pk):
    Dodatek.objects.get(id=pk).delete()
    return render(request, 'usun.html', {})


def Usun_Polecane(request, pk):
    Polecane.objects.get(id=pk).delete()
    return render(request, 'usun.html', {})


################## Edycja ##################

def Edytuj_Produkt(request, pk):
    produkt = get_object_or_404(Produkt, id=pk)

    if request.method == 'POST':
        formularz = Formularz_Produktu(request.POST, instance=produkt)

        if formularz.is_valid():
            produkt = formularz.save(commit=False)
            produkt.save()
            return redirect('Wyswietl_Produkt', pk)

    else:
        formularz = Formularz_Produktu(instance=produkt)

    return render(request, 'edytuj.html', {'formularz': formularz})
