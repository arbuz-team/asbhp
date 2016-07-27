# -*- coding: utf-8 -*-
from wyszukiwarka.views import *
from produkt.views import *
from poczta.views import *
from .forms import *



################## Zakładki: Wyświetlanie ##################

def Wyswietl_Start(request):
    Sprawdz_Sesje(request)
    polecane = Polecane.Pobierz_Aktywne_Oferty()
    return render(request, 'asbhp/start.html',
                            {'polecane':            polecane})




def Wyswietl_O_Firmie(request):
    Sprawdz_Sesje(request)
    css_menu = {'o_firmie': 'wybrany', 'oferta': '',
                'kontakt': '', 'edytuj': ''}

    o_firmie = Zawartosc_Zakladki.objects.get(pk='/o_firmie/')
    return render(request, 'asbhp/o_firmie.html',
                            {'css_menu':            css_menu,
                             'o_firmie':            o_firmie})




def Wyswietl_Oferta(request, wybrana_strona=None, wybrany_filtr=None):

    Sprawdz_Sesje(request, False)

        # potrzebne zmienne
    css_menu = {'o_firmie': '', 'oferta': 'wybrany',
                'kontakt': '', 'edytuj': ''}

    produkt = request.session['produkt']
    request.session['producent'].Ustaw_Pola(request.session['iloczyn'])
    request.session['kolor'].Ustaw_Pola(request.session['iloczyn'])

        # pobieranie listy produktów
    wybrana_strona = int(wybrana_strona) if wybrana_strona else 1
    zawartosc = Pobierz_Zawartosc_Strony(request, produkt, wybrana_strona)

    liczba_stron = zawartosc['liczba_stron']
    produkt = zawartosc['zawartosc_strony']
    numery_stron = Pobierz_Liste_Numerow_Stron(liczba_stron, wybrana_strona)

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
                 'strona':              wybrana_strona,
                 'filtr':               request.session['wybrany_filtr'],
                 'producent':           request.session['producent'].Pobierz_Wybrany()}

    filtr =     {'wyszukiwarka':        request.session['wyszukiwarka'],
                 'producent':           request.session['producent'],
                 'kolor':               request.session['kolor'],
                 'zagrozenia':          request.session['zagrozenia'],
                 'zawody':              request.session['zawody'],
                 'liczba_produktow':    request.session['liczba_produktow']}

    return render(request, 'asbhp/oferta.html',
                            {'css_menu':            css_menu,
                             'produkt':             produkt,
                             'numery_stron':        numery_stron,
                             'kontener':            kontener,
                             'wybrany':             wybrany,
                             'filtr':               filtr})




def Wyswietl_Kontakt(request):
    Sprawdz_Sesje(request)
    Ustaw_Fromularz_Email(request)
    css_menu = {'o_firmie': '', 'oferta': '',
                'kontakt': 'wybrany', 'edytuj': ''}

    kontakt = Zawartosc_Zakladki.objects.get(pk='/kontakt/')
    return render(request, 'asbhp/kontakt.html',
                            {'css_menu':            css_menu,
                             'kontakt':             kontakt,
                             'formularz':           request.session['formularz_poczta']})




def Wyswietl_Edytuj(request):
    Sprawdz_Czy_Zalogowany(request)
    css_menu = {'o_firmie': '', 'oferta': '',
                'kontakt': '', 'edytuj': 'wybrany'}

    produkt = request.session['wyszukane']

        # polecane produkty
    polecane = {'aktywne':      [{'produkt': p,
                                  'formularz': Formularz_Polecane(instance=p)}
                                 for p in Polecane.Pobierz_Aktywne_Oferty()],

                'nieaktywne':   [{'produkt': p,
                                  'formularz': Formularz_Polecane(instance=p)}
                                 for p in Polecane.Pobierz_Nieaktywne_Oferty()]}

        # edycja zakładek 'o_firmie' 'kontakt'
    if not request.session['formularz_o_firmie']:
        o = Zawartosc_Zakladki.objects.get(pk='/o_firmie/')
        request.session['formularz_o_firmie'] = \
            Formularz_Zawartosc_Zakladki(instance=o)

    if not request.session['formularz_kontakt']:
        k = Zawartosc_Zakladki.objects.get(pk='/kontakt/')
        request.session['formularz_kontakt'] = \
            Formularz_Zawartosc_Zakladki(instance=k)

    return render(request, 'asbhp/edytuj.html',
                            {'css_menu':            css_menu,
                             'wyszukiwarka':        request.session['wyszukiwarka'],
                             'produkt':             produkt,
                             'polecane':            polecane,
                             'o_firmie':            request.session['formularz_o_firmie'],
                             'kontakt':             request.session['formularz_kontakt']})




################## Zakładki: Edycja ##################

def Edytuj_O_Firmie_Zapisz(request):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':
        o = Zawartosc_Zakladki.objects.get(pk='/o_firmie/')
        request.session['formularz_o_firmie'] = \
            Formularz_Zawartosc_Zakladki(request.POST, instance=o)

        if request.session['formularz_o_firmie'].is_valid():
            request.session['formularz_o_firmie'].save()

    return redirect('Wyswietl_Edytuj')




def Edytuj_Kontakt_Zapisz(request):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':
        k = Zawartosc_Zakladki.objects.get(pk='/kontakt/')
        request.session['formularz_kontakt'] = \
            Formularz_Zawartosc_Zakladki(request.POST, instance=k)

        if request.session['formularz_kontakt'].is_valid():
            request.session['formularz_kontakt'].save()

    return redirect('Wyswietl_Edytuj')
