# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from forms import *


################## Wyświetlanie ##################

def Wyswietl_Produkt(request, pk):
    produkt = Produkt.objects.filter(id=pk).first()
    return render(request, 'produkt/produkt.html', {'produkt': produkt})


def Wyswietl_Polecane(request):
    polecane = Polecane.objects.all()
    return render(request, 'produkt/polecane.html', {'polecane': polecane})


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

    return render(request, 'produkt/dodaj_produkt.html', {'formularz': formularz})


def Dodaj_Producent(request):

    if request.method == 'POST':
        formularz = Formularz_Producent(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Producent została poprawnie dodana.'
            return render(request, 'produkt/potwierdzenie.html', {'opis': opis})

    else:
        formularz = Formularz_Producent()

    return render(request, 'produkt/dodaj.html', {'formularz': formularz})


def Dodaj_Kolor(request):

    if request.method == 'POST':
        formularz = Formularz_Kolor(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Kolor został poprawnie dodany.'
            return render(request, 'produkt/potwierdzenie.html', {'opis': opis})

    else:
        formularz = Formularz_Kolor()

    return render(request, 'produkt/dodaj.html', {'formularz': formularz})


def Dodaj_Certyfikat(request):

    if request.method == 'POST':
        formularz = Formularz_Certyfikat(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Certyfikat został poprawnie dodany.'
            return render(request, 'produkt/potwierdzenie.html', {'opis': opis})

    else:
        formularz = Formularz_Certyfikat()

    return render(request, 'produkt/dodaj.html', {'formularz': formularz})


def Dodaj_Dodatek(request):

    if request.method == 'POST':
        formularz = Formularz_Dodatek(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Dodatek został poprawnie dodany.'
            return render(request, 'produkt/potwierdzenie.html', {'opis': opis})

    else:
        formularz = Formularz_Dodatek()

    return render(request, 'produkt/dodaj.html', {'formularz': formularz})


def Dodaj_Polecane(request):

    if request.method == 'POST':
        formularz = Formularz_Polecane(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Nowy produkt został poprawnie dodany do ' \
                   'listy produktów polecanych.'
            return render(request, 'produkt/potwierdzenie.html', {'opis': opis})

    else:
        formularz = Formularz_Polecane()

    return render(request, 'produkt/dodaj.html', {'formularz': formularz})


################## Usuwanie ##################

def Usun_Produkt(request, pk):
    Produkt.objects.get(id=pk).delete()
    return render(request, 'produkt/usun.html', {})


def Usun_Producent(request, pk):
    Producent.objects.get(id=pk).delete()
    return render(request, 'produkt/usun.html', {})


def Usun_Kolor(request, pk):
    Kolor.objects.get(id=pk).delete()
    return render(request, 'produkt/usun.html', {})


def Usun_Certyfikat(request, pk):
    Certyfikat.objects.get(id=pk).delete()
    return render(request, 'produkt/usun.html', {})


def Usun_Dodatek(request, pk):
    Dodatek.objects.get(id=pk).delete()
    return render(request, 'produkt/usun.html', {})


def Usun_Polecane(request, pk):
    Polecane.objects.get(id=pk).delete()
    return render(request, 'produkt/usun.html', {})


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

    return render(request, 'produkt/edytuj.html', {'formularz': formularz})
