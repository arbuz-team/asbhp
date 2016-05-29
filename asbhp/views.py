# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from forms import *

################## Zakładki ##################

def Start(request):
    return render(request, 'start.html', {})

def O_Firmie(request):
    return render(request, 'o_firmie.html', {})

def Oferta(request):
    return Lista_Produktow(request)

def Kontakt(request):
    return render(request, 'kontakt.html', {})

################## Opcje ##################

def Lista_Produktow(request):
    produkty = Produkt.objects.all()
    return render(request, 'lista.html', {'produkty': produkty})

def Wyswietl_Produkt(request, pk):
    produkt = Produkt.objects.filter(id=pk).first()
    return render(request, 'produkt.html', {'produkt': produkt})

def Dodaj_Produkt(request):

    if request.method == 'POST':
        formularz = Formularz_Produktu(request.POST)

        if formularz.is_valid():
            formularz.save()
            return redirect('Lista_Produktow')

    else:
        formularz = Formularz_Produktu()

    return render(request, 'edytuj.html', {'formularz': formularz})
