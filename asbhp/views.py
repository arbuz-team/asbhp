# -*- coding: utf-8 -*-
from wyszukiwarka.views import *
from produkt.views import *
from poczta.views import *
from forms import *



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




def Wyswietl_Oferta(request, wybrany_strona=None, wybrany_filtr=None):

    Sprawdz_Sesje(request, False)

        # potrzebne zmienne
    css_menu = {'o_firmie': '', 'oferta': 'wybrany',
                'kontakt': '', 'edytuj': ''}

    produkt = Iloczyn_Zbiorow(Filtruj(request), Konteneruj(request))
    request.session['producent'].Ustaw_Pola(Iloczyn_Zbiorow(Wyszukaj(request), Konteneruj(request)))
    request.session['kolor'].Ustaw_Pola(Iloczyn_Zbiorow(Wyszukaj(request), Konteneruj(request)))

        # pobieranie listy produktów
    wynik = Pobierz_Listy_Produktow(request, produkt)
    produkt = wynik[(int(wybrany_strona) - 1) if wybrany_strona else 0]

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
                            {'css_menu':            css_menu,
                             'produkt':             produkt,
                             'numery_stron':        range(1, len(wynik) + 1),
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

    produkt = Filtruj(request)

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
