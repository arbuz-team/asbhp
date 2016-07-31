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

    return render(request, 'asbhp/o_firmie.html',
                            {'css_menu':            css_menu})




def Wyswietl_Oferta(request, wybrana_strona=None):

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

        # podział zmiennych na klasy
    kontener =  {'typ':                 request.session['typ'],
                 'dziedzina':           request.session['dziedzina'],
                 'rodzaj':              request.session['rodzaj']}

    wybrany =   {'typ':                 request.session['wybrany_typ'],
                 'dziedzina':           request.session['wybrany_dziedzina'],
                 'rodzaj':              request.session['wybrany_rodzaj'],
                 'strona':              wybrana_strona,
                 'filtr':               request.session['wybrany_filtr'],
                 'wyszukiwanie':        request.session['wyszukiwarka'].Pobierz_Wybrany(),
                 'producent':           request.session['producent'].Pobierz_Wybrany(),
                 'kolor':               request.session['kolor'].Pobierz_Wybrany(),
                 'zagrozenia':          request.session['zagrozenia'].Pobierz_Wybrany(),
                 'zawody':              request.session['zawody'].Pobierz_Wybrany(),
                 'wyswietlanie':        request.session['liczba_produktow'].Pobierz_Wybrany()}

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
    godziny = Zawartosc_Zakladki.objects.get(pk='/kontakt/2')
    return render(request, 'asbhp/kontakt.html',
                            {'css_menu':            css_menu,
                             'kontakt':             kontakt,
                             'godziny':             godziny,
                             'formularz':           request.session['formularz_poczta']})




def Wyswietl_Edytuj(request, wybrana_strona='1'):
    Sprawdz_Czy_Zalogowany(request)
    css_menu = {'o_firmie': '', 'oferta': '',
                'kontakt': '', 'edytuj': 'wybrany'}

    produkt = request.session['wyszukane']
    wybrana_strona = int(wybrana_strona)
    zawartosc = Pobierz_Zawartosc_Strony(request, produkt, wybrana_strona)

    liczba_stron = zawartosc['liczba_stron']
    produkt = zawartosc['zawartosc_strony']
    numery_stron = Pobierz_Liste_Numerow_Stron(liczba_stron, wybrana_strona)


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

    if not request.session['formularz_kontakt_2']:
        k = Zawartosc_Zakladki.objects.get(pk='/kontakt/2')
        request.session['formularz_kontakt_2'] = \
            Formularz_Zawartosc_Zakladki(instance=k)

    return render(request, 'asbhp/edytuj.html',
                            {'css_menu':            css_menu,
                             'wyszukiwarka':        request.session['wyszukiwarka'],
                             'produkt':             produkt,
                             'numery_stron':        numery_stron,
                             'wybrana_strona':      wybrana_strona,
                             'polecane':            polecane,
                             'o_firmie':            request.session['formularz_o_firmie'],
                             'kontakt':             request.session['formularz_kontakt'],
                             'godziny':             request.session['formularz_kontakt_2']})




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




def Edytuj_Kontakt_Godziny_Zapisz(request):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':
        k = Zawartosc_Zakladki.objects.get(pk='/kontakt/2')
        request.session['formularz_kontakt_2'] = \
            Formularz_Zawartosc_Zakladki(request.POST, instance=k)

        if request.session['formularz_kontakt_2'].is_valid():
            request.session['formularz_kontakt_2'].save()

    return redirect('Wyswietl_Edytuj')




################## Zakładki: Dodatki ##################

def Wybrana_Zakladka_Edycji(request, numer_zakladki):
    request.session['wybrana_zakladka_edycji'] = numer_zakladki
    request.session['potwierdzenie'] = \
        'Wybrałeś zakładkę o numerze: {0}.'.format(numer_zakladki)

    return redirect('Wyswietl_Potwierdzenie')
