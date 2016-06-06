# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from produkt.models import *
from forms import *

################## Zakładki ##################

def Wyswietl_Start(request):
    polecane = Polecane.objects.all()
    return render(request, 'asbhp/start.html', {'polecane': polecane})


def Wyswietl_O_Firmie(request):
    css_menu = ['wybrany', '', '']
    return render(request, 'asbhp/o_firmie.html', {'css_menu': css_menu})


def Wyswietl_Oferta(request):
    css_menu = ['', 'wybrany', '']
    typ = Typ_Odziezy.objects.all()
    dziedzina = Dziedzina_Odziezy.objects.all()
    rodzaj = Rodzaj_Odziezy.objects.all()
    return render(request, 'asbhp/oferta.html', {'css_menu': css_menu,
                                                 'typ': typ,
                                                 'dziedzina': dziedzina,
                                                 'rodzaj': rodzaj})


def Wyswietl_Kontakt(request):
    css_menu = ['', '', 'wybrany']
    kontakt = Kontakt.objects.all()
    return render(request, 'asbhp/kontakt.html', {'css_menu': css_menu,
                                                  'kontakt': kontakt})

def Edytuj_Kontakt(request):
    kontakt = Kontakt.objects.all()
    lista_formularzy = []

    for k in kontakt:
        lista_formularzy.append(Formularz_Kontakt(instance=k))

    return render(request, 'asbhp/edytuj_kontakt.html', {'lista_formularzy': lista_formularzy})


def Edytuj_Kontakt_Zapisz(request, pk):

    if request.method == 'POST':
        kontakt = Kontakt.objects.get(id=pk)
        formularz = Formularz_Kontakt(request.POST, instance=kontakt)

        if formularz.is_valid():
            formularz.save()
            return redirect('Wyswietl_Kontakt')

    return redirect('Edytuj_Kontakt')
