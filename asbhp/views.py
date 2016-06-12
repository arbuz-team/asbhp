# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from wyszukiwarka.views import *
from produkt.models import *
from forms import *

################## Zakładki: Wyświetlanie ##################

def Wyswietl_Start(request):
    polecane = Polecane.objects.all()
    return render(request, 'asbhp/start.html',
                  {'polecane': polecane})


def Wyswietl_O_Firmie(request):
    css_menu = ['wybrany', '', '']
    o_firmie = O_Firmie.objects.all()
    return render(request, 'asbhp/o_firmie.html',
                  {'css_menu': css_menu,
                   'o_firmie': o_firmie})


def Wyswietl_Oferta(request, wybrany_strona=None, wybrany_filtr=None):

        # pobieranie formularza - działanie komunikatów
    if 'wyszukiwarka' in request.session:
        wyszukiwarka = request.session['wyszukiwarka']

    else:
        wyszukiwarka = Pobierz_Formularz_Wyszukiwarki(request)

        # potrzebne zmienne
    css_menu = ['', 'wybrany', '']
    produkt = Produkt.objects.all()

    typ = Typ_Odziezy.objects.all()
    dziedzina = []
    rodzaj = []

    wybrany_typ = []
    wybrany_dziedzina = []
    wybrany_rodzaj = []

        # wybrany kontener typ
    if 'wybrany_typ' in request.session:
        wybrany_typ = request.session['wybrany_typ']
        dziedzina = Dziedzina_Odziezy.objects.filter(typ__url=wybrany_typ)
        produkt = produkt.filter(rodzaj__dziedzina__typ__url=wybrany_typ)

        # wybrany kontener dziedzina
    if 'wybrany_dziedzina' in request.session:
        wybrany_dziedzina = request.session['wybrany_dziedzina']
        rodzaj = Rodzaj_Odziezy.objects.filter(dziedzina__url=wybrany_dziedzina)
        produkt = produkt.filter(rodzaj__dziedzina__url=wybrany_dziedzina)

        # wybrany kontener rodzaj
    if 'wybrany_rodzaj' in request.session:
        wybrany_rodzaj = request.session['wybrany_rodzaj']
        produkt = produkt.filter(rodzaj__url=wybrany_rodzaj)

        # filtrowane produkty
    if 'wyszukane_produkty' in request.session:
        iloczyn = []
        for w in request.session['wyszukane_produkty']:
            if w in produkt:
                iloczyn.append(w)

        produkt = iloczyn

        # pobieranie listy produktów
    wynik = Pobierz_Listy_Produktow(request, produkt)
    produkt = wynik[int(wybrany_strona) if wybrany_strona else 0]

        # wybrany filtr = liczba (format: f_<liczba>)
    if wybrany_filtr:
        request.session['wybrany_filtr'] = wybrany_filtr[2]

    if 'wybrany_filtr' not in request.session:
        request.session['wybrany_filtr'] = 1

    return render(request, 'asbhp/oferta.html',
                  {'wyszukiwarka': wyszukiwarka,
                   'css_menu': css_menu,
                   'produkt': produkt,
                   'numery_stron': range(1, len(wynik) + 1),
                   'typ': typ,
                   'dziedzina': dziedzina,
                   'rodzaj': rodzaj,
                   'wybrany_typ': wybrany_typ,
                   'wybrany_dziedzina': wybrany_dziedzina,
                   'wybrany_rodzaj': wybrany_rodzaj,
                   'wybrany_strona': wybrany_strona,
                   'wybrany_filtr': request.session['wybrany_filtr'],
                   'filtr_producent': Formularz_Filtru_Producent(),
                   'filtr_kolor': Formularz_Filtru_Kolor(),
                   'filtr_zagrozenia': Formularz_Filtru_Zagrozenia(),
                   'filtr_zawody': Formularz_Filtru_Zawody(),
                   'filtr_liczba_produktow': Formularz_Filtru_Liczba_Produktow()})

def Wyswietl_Kontakt(request):
    css_menu = ['', '', 'wybrany']
    kontakt = Kontakt.objects.all()
    return render(request, 'asbhp/kontakt.html',
                  {'css_menu': css_menu,
                   'kontakt': kontakt})


################## Zakładki: Edycja ##################

def Edytuj_O_Firmie(request):
    o_firmie = O_Firmie.objects.all()
    lista_formularzy = []

    for o in o_firmie:
        lista_formularzy.append(Formularz_O_Firmie(instance=o))

    return render(request, 'asbhp/edytuj.html',
                  {'lista_formularzy': lista_formularzy})


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

    return render(request, 'asbhp/edytuj.html',
                  {'lista_formularzy': lista_formularzy})


def Edytuj_Kontakt_Zapisz(request, pk):

    if request.method == 'POST':
        kontakt = Kontakt.objects.get(id=pk)
        formularz = Formularz_Kontakt(request.POST, instance=kontakt)

        if formularz.is_valid():
            formularz.save()
            return redirect('Wyswietl_Kontakt')

    return redirect('Edytuj_Kontakt')


################## Funkcje dodatkowe ##################

def Pobierz_Listy_Produktow(request, produkt):

    wynik = []
    if 'liczba_produktow' not in request.session:
        request.session['liczba_produktow'] = 4

    liczba = int(request.session['liczba_produktow'])

        # tworzę listę zawierającą listy po określonej
        # ilości produktów w zmiennej liczba
    for i in range(0, (len(produkt) / liczba) + 1):
        wynik.append(produkt[i * liczba: (i * liczba) + liczba])

    return wynik
