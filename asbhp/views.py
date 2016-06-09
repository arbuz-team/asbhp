# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from wyszukiwarka.views import *
from produkt.models import *
from forms import *

################## Zakładki: Wyświetlanie ##################

def Wyswietl_Start(request):
    polecane = Polecane.objects.all()
    return render(request, 'asbhp/start.html', {'polecane': polecane})


def Wyswietl_O_Firmie(request):
    css_menu = ['wybrany', '', '']
    o_firmie = O_Firmie.objects.all()
    return render(request, 'asbhp/o_firmie.html', {'css_menu': css_menu,
                                                   'o_firmie': o_firmie})


def Wyswietl_Oferta(request):

    if 'wyszukiwarka' in request.session:
        wyszukiwarka = request.session['wyszukiwarka']

    else:
        wyszukiwarka = Pobierz_Formularz_Wyszukiwarki(request)

    css_menu = ['', 'wybrany', '']
    produkt = Produkt.objects.all()
    typ = Typ_Odziezy.objects.all()
    dziedzina = []
    rodzaj = []

    wybrany_typ = []
    wybrany_dziedzina = []
    wybrany_rodzaj = []

    if 'wybrany_typ' in request.session:
        wybrany_typ = request.session['wybrany_typ']
        dziedzina = Dziedzina_Odziezy.objects.filter(typ__url=wybrany_typ)
        produkt = produkt.filter(rodzaj__dziedzina__typ__url=wybrany_typ)

    if 'wybrany_dziedzina' in request.session:
        wybrany_dziedzina = request.session['wybrany_dziedzina']
        rodzaj = Rodzaj_Odziezy.objects.filter(dziedzina__url=wybrany_dziedzina)
        produkt = produkt.filter(rodzaj__dziedzina__url=wybrany_dziedzina)

    if 'wybrany_rodzaj' in request.session:
        wybrany_rodzaj = request.session['wybrany_rodzaj']
        produkt = produkt.filter(rodzaj__url=wybrany_rodzaj)

    if 'wyszukane_produkty' in request.session:
        wynik = []
        for w in request.session['wyszukane_produkty']:
            if w in produkt:
                wynik.append(w)

        produkt = wynik

    return render(request, 'asbhp/oferta.html', {'wyszukiwarka': wyszukiwarka,
                                                 'css_menu': css_menu,
                                                 'produkt': produkt,
                                                 'typ': typ,
                                                 'dziedzina': dziedzina,
                                                 'rodzaj': rodzaj,
                                                 'wybrany_typ': wybrany_typ,
                                                 'wybrany_dziedzina': wybrany_dziedzina,
                                                 'wybrany_rodzaj': wybrany_rodzaj,
                                                 'filtr_producent': Formularz_Filtru_Producent(),
                                                 'filtr_kolor': Formularz_Filtru_Kolor(),
                                                 'filtr_zagrozenia': Formularz_Filtru_Zagrozenia(),
                                                 'filtr_zawody': Formularz_Filtru_Zawody()})


def Wyswietl_Kontakt(request):
    css_menu = ['', '', 'wybrany']
    kontakt = Kontakt.objects.all()
    return render(request, 'asbhp/kontakt.html', {'css_menu': css_menu,
                                                  'kontakt': kontakt})


################## Zakładki: Edycja ##################

def Edytuj_O_Firmie(request):
    o_firmie = O_Firmie.objects.all()
    lista_formularzy = []

    for o in o_firmie:
        lista_formularzy.append(Formularz_O_Firmie(instance=o))

    return render(request, 'asbhp/edytuj.html', {'lista_formularzy': lista_formularzy})


def Edytuj_O_Firmie_Zapisz(request, pk):

    if request.method == 'POST':
        o_firmie = O_Firmie.objects.get(id=pk)
        formularz = Formularz_O_Firmie(request.POST, instance=o_firmie)

        if formularz.is_valid():
            formularz.save()
            return redirect('Wyswietl_O_Firmie')

    return redirect('Edytuj_O_Firmie')


def Edytuj_Kontakt(request):
    kontakt = Kontakt.objects.all()
    lista_formularzy = []

    for k in kontakt:
        lista_formularzy.append(Formularz_Kontakt(instance=k))

    return render(request, 'asbhp/edytuj.html', {'lista_formularzy': lista_formularzy})


def Edytuj_Kontakt_Zapisz(request, pk):

    if request.method == 'POST':
        kontakt = Kontakt.objects.get(id=pk)
        formularz = Formularz_Kontakt(request.POST, instance=kontakt)

        if formularz.is_valid():
            formularz.save()
            return redirect('Wyswietl_Kontakt')

    return redirect('Edytuj_Kontakt')