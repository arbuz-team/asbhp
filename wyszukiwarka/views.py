# -*- coding: utf-8 -*-
from dodatek.views import *

################## Wyszukiwarka ##################

def Wyszukaj(request):

    wynik = Produkt.objects.all()
    wyszukiwarka = request.session['wyszukiwarka']

    if wyszukiwarka.is_valid():
        zapytanie = wyszukiwarka.cleaned_data['zapytanie'].split(' ')

        wynik_sql = Produkt.objects.filter(
            reduce(operator.or_, (Q(nazwa__icontains=s) for s in zapytanie))        |
            reduce(operator.or_, (Q(opis__icontains=s) for s in zapytanie))         |
            reduce(operator.or_, (Q(slowa_kluczowe__icontains=s) for s in zapytanie)) |
            reduce(operator.or_, (Q(producent__nazwa__icontains=s) for s in zapytanie)) |
            reduce(operator.or_, (Q(kolor__nazwa__icontains=s) for s in zapytanie)) |
            reduce(operator.or_, (Q(rodzaj__nazwa__icontains=s) for s in zapytanie)) |
            reduce(operator.or_, (Q(rodzaj__dziedzina__nazwa__icontains=s) for s in zapytanie)) |
            reduce(operator.or_, (Q(rodzaj__dziedzina__typ__nazwa__icontains=s) for s in zapytanie))
        )

            # p - pojedynczy produkt
        pobierz_nazwa = lambda pole: pole.nazwa if pole else ''
        pobierz = lambda pole: pole if pole else ''
        wynik_str = [(index, (p.nazwa + p.opis +
                              pobierz_nazwa(p.producent) +
                              pobierz_nazwa(p.kolor) +
                              pobierz(p.slowa_kluczowe) +
                              p.rodzaj.nazwa +
                              p.rodzaj.dziedzina.nazwa +
                              p.rodzaj.dziedzina.typ.nazwa).lower())
                     for index, p in enumerate(wynik_sql)]

            # tworzę listę krotek określających pozycje produktów
        pozycja = []
        for produkt in wynik_str:
            trafienia = 0
            for slowo in zapytanie:
                trafienia += produkt[1].count(slowo.lower())
            pozycja.append((trafienia, produkt[0])) # (trafienia, id)

        pozycja.sort(reverse=True)

            # tworzę posortowaną listę produktów
        wynik = []
        for produkt in pozycja:
            wynik.append(wynik_sql[produkt[1]]) # produkt[1], to index

    return wynik


def Usun_Sesje_Wyszukiwarki(request):

    if 'wyszukane_produkty' in request.session:
        del request.session['wyszukane_produkty']

    if 'wyszukiwarka' in request.session:
        del request.session['wyszukiwarka']

    return redirect('Wyswietl_Oferta')


def Usun_Sesje_Filtrow(request):
    Usun_Sesje(request)
    return redirect('Wyswietl_Oferta')


################## Filtry ##################

def Filtr_Wyszukiwarka(request):

    if request.method == 'POST':
        filtr = Formularz_Wyszukiwarki(request.POST)
        request.session['wyszukiwarka'] = filtr

        if filtr.is_valid():
            pass

    return redirect('Wyswietl_Oferta')


def Filtr_Producent(request):

    if request.method == 'POST':
        filtr = Formularz_Filtru_Producent(request.POST)
        request.session['producent'] = filtr

        if filtr.Waliduj():
            pass

    return redirect('Wyswietl_Oferta')


def Filtr_Kolor(request):

    if request.method == 'POST':
        filtr = Formularz_Filtru_Kolor(request.POST)
        request.session['kolor'] = filtr

        if filtr.Waliduj():
            pass

    return redirect('Wyswietl_Oferta')


def Filtr_Zagrozenia(request):

    if request.method == 'POST':
        filtr = Formularz_Filtru_Zagrozenia(request.POST)
        request.session['zagrozenia'] = filtr

        if filtr.is_valid():
            pass

    return redirect('Wyswietl_Oferta')


def Filtr_Zawody(request):

    if request.method == 'POST':
        filtr = Formularz_Filtru_Zawody(request.POST)
        request.session['zawody'] = filtr

        if filtr.is_valid():
            pass

    return redirect('Wyswietl_Oferta')


def Filtr_Liczba_Produktow(request):

    if request.method == 'POST':
        filtr = Formularz_Filtru_Liczba_Produktow(request.POST)
        request.session['liczba_produktow'] = filtr

        if filtr.is_valid():
            pass

    return redirect('Wyswietl_Oferta')


def Filtruj(request):
    wynik = Produkt.objects.all()

    if request.session['wyszukiwarka'].is_valid():
        wynik = Wyszukaj(request)

    if request.session['producent'].Waliduj():
        wynik = Iloczyn_Zbiorow(wynik, Produkt.objects.filter(
            producent__pk=request.session['producent'].Pobierz_Wybrany()))

    if request.session['kolor'].Waliduj():
        wynik = Iloczyn_Zbiorow(wynik, Produkt.objects.filter(
            kolor__pk=request.session['kolor'].Pobierz_Wybrany()))

    if request.session['zagrozenia'].is_valid():
        if request.session['zagrozenia'].cleaned_data['zagrozenia']:
            wynik = Iloczyn_Zbiorow(wynik, Produkt.objects.filter(
                zagrozenia=request.session['zagrozenia'].cleaned_data['zagrozenia']))

    if request.session['zawody'].is_valid():
        if request.session['zawody'].cleaned_data['zawody']:
            wynik = Iloczyn_Zbiorow(wynik, Produkt.objects.filter(
                zawody=request.session['zawody'].cleaned_data['zawody']))

    return wynik


################## Kontenery ##################

def Kontener_Typ(request):

    request.session['dziedzina'] = []
    request.session['rodzaj'] = []
    request.session['wybrany_dziedzina'] = None
    request.session['wybrany_rodzaj'] = None

    if request.method == 'POST':
        kontener = Formularz_Kontener(request.POST)

        if kontener.is_valid():
            request.session['wybrany_typ'] = \
                kontener.cleaned_data['zawartosc']

        else:
            del request.session['wybrany_typ']

    return redirect('Wyswietl_Oferta')


def Kontener_Dziedzina(request):

    request.session['rodzaj'] = []
    request.session['wybrany_rodzaj'] = None

    if request.method == 'POST':
        kontener = Formularz_Kontener(request.POST)

        if kontener.is_valid():
            request.session['wybrany_dziedzina'] = \
                kontener.cleaned_data['zawartosc']

        else:
            del request.session['wybrany_dziedzina']

    return redirect('Wyswietl_Oferta')


def Kontener_Rodzaj(request):

    if request.method == 'POST':
        kontener = Formularz_Kontener(request.POST)

        if kontener.is_valid():
            request.session['wybrany_rodzaj'] = \
                kontener.cleaned_data['zawartosc']

        else:
            del request.session['wybrany_rodzaj']

    return redirect('Wyswietl_Oferta')


def Konteneruj(request):
    wynik = Produkt.objects.all()

        # wybrany kontener typ
    if request.session['wybrany_typ']:
        wybrany_typ = request.session['wybrany_typ']
        wynik = wynik.filter(rodzaj__dziedzina__typ__url=wybrany_typ)
        request.session['dziedzina'] = Dziedzina_Odziezy.objects\
            .filter(typ__url=wybrany_typ)

            # wybrany kontener dziedzina
        if request.session['wybrany_dziedzina']:
            wybrany_dziedzina = request.session['wybrany_dziedzina']
            wynik = wynik.filter(rodzaj__dziedzina__url=wybrany_dziedzina)
            request.session['rodzaj'] = Rodzaj_Odziezy.objects\
                .filter(dziedzina__url=wybrany_dziedzina)

                # wybrany kontener rodzaj
            if request.session['wybrany_rodzaj']:
                wybrany_rodzaj = request.session['wybrany_rodzaj']
                wynik = wynik.filter(rodzaj__url=wybrany_rodzaj)

    return wynik
