# -*- coding: utf-8 -*-
from dodatek.views import *

################## Wyświetlanie ##################

def Wyswietl_Produkt(request, pk):
    request.session['wybrany_produkt'] = Produkt.objects.filter(id=pk).first()
    return redirect('Wyswietl_Oferta')


def Wyswietl_Polecane(request):
    polecane = Polecane.objects.all()
    return render(request, 'produkt/polecane.html',
                            {'polecane': polecane})


################## Dodawanie ##################

def Dodaj_Produkt(request):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':
        formularz = Formularz_Produktu(request.POST, request.FILES)

        if formularz.is_valid():
            produkt = formularz.save()
            Zarzadzaj_Zdjeciem_Produktu(produkt, formularz)
            return redirect('Wyswietl_Produkt', produkt.pk)

    else:
        formularz = Formularz_Produktu()

        # usunięcie etykiet dla prawie wszystkich pól
    for f in formularz:
        if f.label not in ['Certyfikaty', 'Zagrozenia', 'Zawody']:
            f.label = ''

    return render(request, 'produkt/dodaj_produkt.html',
                            {'formularz': formularz})


def Dodaj_Producent(request):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':
        formularz = Formularz_Producent(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Producent została poprawnie dodana.'
            return render(request, 'produkt/potwierdzenie.html',
                                    {'opis': opis})

    else:
        formularz = Formularz_Producent()

    return render(request, 'produkt/dodaj.html',
                  {'formularz': formularz})


def Dodaj_Kolor(request):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':
        formularz = Formularz_Kolor(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Kolor został poprawnie dodany.'
            return render(request, 'produkt/potwierdzenie.html',
                                    {'opis': opis})

    else:
        formularz = Formularz_Kolor()

    return render(request, 'produkt/dodaj.html',
                            {'formularz': formularz})


def Dodaj_Certyfikat(request):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':
        formularz = Formularz_Certyfikat(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Certyfikat został poprawnie dodany.'
            return render(request, 'produkt/potwierdzenie.html',
                                    {'opis': opis})

    else:
        formularz = Formularz_Certyfikat()

    return render(request, 'produkt/dodaj.html',
                            {'formularz': formularz})


def Dodaj_Dodatek(request):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':
        formularz = Formularz_Dodatek(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Dodatek został poprawnie dodany.'
            return render(request, 'produkt/potwierdzenie.html',
                                    {'opis': opis})

    else:
        formularz = Formularz_Dodatek()

    return render(request, 'produkt/dodaj.html',
                            {'formularz': formularz})


def Dodaj_Polecane(request):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':
        formularz = Formularz_Polecane(request.POST)

        if formularz.is_valid():
            formularz.save()
            opis = 'Nowy produkt został poprawnie dodany do ' \
                   'listy produktów polecanych.'
            return render(request, 'produkt/potwierdzenie.html',
                                    {'opis': opis})

    else:
        formularz = Formularz_Polecane()

    return render(request, 'produkt/dodaj.html',
                            {'formularz': formularz})


################## Usuwanie ##################

def Usun_Produkt(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    Produkt.objects.get(id=pk).delete()
    return render(request, 'produkt/usun.html', {})


def Usun_Producent(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    Producent.objects.get(id=pk).delete()
    return render(request, 'produkt/usun.html', {})


def Usun_Kolor(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    Kolor.objects.get(id=pk).delete()
    return render(request, 'produkt/usun.html', {})


def Usun_Certyfikat(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    Certyfikat.objects.get(id=pk).delete()
    return render(request, 'produkt/usun.html', {})


def Usun_Dodatek(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    Dodatek.objects.get(id=pk).delete()
    return render(request, 'produkt/usun.html', {})


def Usun_Polecane(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    Polecane.objects.get(id=pk).delete()
    return render(request, 'produkt/usun.html', {})


################## Edycja ##################

def Edytuj_Produkt(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    produkt = get_object_or_404(Produkt, id=pk)

    if request.method == 'POST':
        formularz = Formularz_Produktu(request.POST, request.FILES,
                                       instance=produkt)

        if formularz.is_valid():
            produkt = formularz.save(commit=False)
            produkt.save()
            Zarzadzaj_Zdjeciem_Produktu(produkt, formularz)
            return redirect('Wyswietl_Produkt', pk)

    else:
        formularz = Formularz_Produktu(instance=produkt)

    return render(request, 'produkt/edytuj.html',
                            {'formularz': formularz})


################## Dodatki ##################

def Zarzadzaj_Zdjeciem_Produktu(produkt, formularz):

    if formularz.cleaned_data['zewnetrzny_url']:
        produkt.Zapisz_Zdjecie_URL(formularz.cleaned_data['zewnetrzny_url'])

    if formularz.cleaned_data['zdjecie']:
        if '/static/img/produkt/' not in str(formularz.cleaned_data['zdjecie']):
            produkt.Zapisz_Zdjecie_Formularz()
