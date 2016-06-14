# -*- coding: utf-8 -*-
from wyszukiwarka.views import *
from produkt.views import *
from forms import *

################## Zakładki: Wyświetlanie ##################

def Wyswietl_Start(request):
    polecane = Polecane.objects.all()
    return render(request, 'asbhp/start.html',
                            {'polecane':          polecane})


def Wyswietl_O_Firmie(request):
    css_menu = ['wybrany', '', '']
    o_firmie = O_Firmie.objects.all()
    return render(request, 'asbhp/o_firmie.html',
                            {'css_menu':          css_menu,
                             'o_firmie':          o_firmie})


def Wyswietl_Oferta(request, wybrany_strona=None, wybrany_filtr=None):

    Sprawdz_Sesje(request)

        # potrzebne zmienne
    css_menu = ['', 'wybrany', '']
    produkt = Iloczyn_Zbiorow(Filtruj(request), Konteneruj(request))

        # pobieranie listy produktów
    wynik = Pobierz_Listy_Produktow(request, produkt)
    produkt = wynik[int(wybrany_strona) if wybrany_strona else 0]

        # wybrany filtr = liczba (format: f_<liczba>)
    if wybrany_filtr:
        request.session['wybrany_filtr'] = wybrany_filtr[2]

    if 'wybrany_filtr' not in request.session:
        request.session['wybrany_filtr'] = 1

        # podział zmiennych na klasy
    kontener =  {'typ':                 request.session['typ'],
                 'dziedzina':           request.session['dziedzina'],
                 'rodzaj':              request.session['rodzaj']}

    wybrany =   {'typ':                 request.session['wybrany_typ'],
                 'dziedzina':           request.session['wybrany_dziedzina'],
                 'rodzaj':              request.session['wybrany_rodzaj'],
                 'strona':              wybrany_strona,
                 'filtr':               request.session['wybrany_filtr']}

    filtr =     {'wyszukiwarka':        request.session['wyszukiwarka'],
                 'producent':           request.session['producent'],
                 'kolor':               request.session['kolor'],
                 'zagrozenia':          request.session['zagrozenia'],
                 'zawody':              request.session['zawody'],
                 'liczba_produktow':    request.session['liczba_produktow']}

    return render(request, 'asbhp/oferta.html',
                            {'css_menu':          css_menu,
                             'produkt':           produkt,
                             'numery_stron':      range(1, len(wynik) + 1),
                             'kontener':          kontener,
                             'wybrany':           wybrany,
                             'filtr':             filtr})


def Wyswietl_Kontakt(request):
    css_menu = ['', '', 'wybrany']
    kontakt = Kontakt.objects.all()
    return render(request, 'asbhp/kontakt.html',
                            {'css_menu':          css_menu,
                             'kontakt':           kontakt})


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
