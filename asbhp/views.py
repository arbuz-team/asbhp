# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from forms import *

################## Zakładki ##################

def Start(request):
    return render(request, 'start.html', {})


def O_Firmie(request):
    css_menu = ['wybrany', '', '']
    return render(request, 'o_firmie.html', {"css_menu": css_menu})


def Oferta(request):
    css_menu = ['', 'wybrany', '']
    return render(request, 'oferta.html', {"css_menu": css_menu})


def Kontakt(request):
    css_menu = ['', '', 'wybrany']
    return render(request, 'kontakt.html', {"css_menu": css_menu})


################## Opcje ##################

def Lista_Produktow(request):
    produkty = Produkt.objects.all()
    return render(request, 'lista.html', {'produkty': produkty})


def Wyswietl_Produkt(request, pk):
    produkt = Produkt.objects.filter(id=pk).first()
    return render(request, 'produkt.html', {'produkt': produkt})


################## Dodawanie ##################

def Dodaj_Produkt(request):

    if request.method == 'POST':
        formularz = Formularz_Produktu(request.POST)

        if formularz.is_valid():
            formularz.save()
            return redirect('Lista_Produktow')

    else:
        formularz = Formularz_Produktu()

    return render(request, 'dodaj.html', {'formularz': formularz})


def Dodaj_Opis(request):

    if request.method == 'POST':
        formularz = Formularz_Opis(request.POST)

        if formularz.is_valid():
            formularz.save()
            return redirect('Lista_Produktow')

    else:
        formularz = Formularz_Opis()

    return render(request, 'dodaj.html', {'formularz': formularz})


def Dodaj_Firma(request):

    if request.method == 'POST':
        formularz = Formularz_Firma(request.POST)

        if formularz.is_valid():
            formularz.save()
            return redirect('Lista_Produktow')

    else:
        formularz = Formularz_Firma()

    return render(request, 'dodaj.html', {'formularz': formularz})


def Dodaj_Kolor(request):

    if request.method == 'POST':
        formularz = Formularz_Kolor(request.POST)

        if formularz.is_valid():
            formularz.save()
            return redirect('Lista_Produktow')

    else:
        formularz = Formularz_Kolor()

    return render(request, 'dodaj.html', {'formularz': formularz})


def Dodaj_Certyfikat(request):

    if request.method == 'POST':
        formularz = Formularz_Certyfikat(request.POST)

        if formularz.is_valid():
            formularz.save()
            return redirect('Lista_Produktow')

    else:
        formularz = Formularz_Certyfikat()

    return render(request, 'dodaj.html', {'formularz': formularz})


def Dodaj_Dodatek(request):

    if request.method == 'POST':
        formularz = Formularz_Dodatek(request.POST)

        if formularz.is_valid():
            formularz.save()
            return redirect('Lista_Produktow')

    else:
        formularz = Formularz_Dodatek()

    return render(request, 'dodaj.html', {'formularz': formularz})


def Dodaj_Polecane(request):

    if request.method == 'POST':
        formularz = Formularz_Polecane(request.POST)

        if formularz.is_valid():
            formularz.save()
            return redirect('Lista_Produktow')

    else:
        formularz = Formularz_Polecane()

    return render(request, 'dodaj.html', {'formularz': formularz})
