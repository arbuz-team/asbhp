# -*- coding: utf-8 -*-
from dodatek.views import *
from asbhp.views import Wyswietl_Oferta



################## Wyświetlanie ##################

def Wyswietl_Produkt(request, pk):
    return Wyswietl_Oferta(request)




################## Dodawanie ##################

def Dodaj_Produkt(request):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':
        formularz = Formularz_Produktu(request.POST, request.FILES)

        if formularz.is_valid():
            produkt = formularz.save()
            Zarzadzaj_Zdjeciem_Produktu(produkt, formularz)

            Meta_Tagi.objects.create(
                adres_strony='/produkt/%s/' % str(produkt.pk),
                description=produkt.opis[0:154],
                og_type='produkt',
                og_url='http://asbhp.arbuz.team/produkt/%s/' % str(produkt.pk),
                og_image=str(produkt.zdjecie)
            ).save()

            request.session['potwierdzenie'] = \
                'Produkt został poprawnie dodany.'
            return redirect('/komunikat/potwierdzenie/')

    else:
        formularz = Formularz_Produktu()

        # usunięcie etykiet dla prawie wszystkich pól
    for f in formularz:
        if f.label not in ['Certyfikaty', 'Zagrozenia', 'Zawody']:
            f.label = ''

    return render(request, 'produkt/dodaj.html',
                            {'formularz': formularz})




def Dodaj_Producent(request):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':
        formularz = Formularz_Producent(request.POST)

        if formularz.is_valid():
            formularz.save()
            request.session['potwierdzenie'] = \
                'Producent została poprawnie dodana.'
            return redirect('/komunikat/potwierdzenie/')

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
            request.session['potwierdzenie'] = \
                'Kolor został poprawnie dodany.'
            return redirect('/komunikat/potwierdzenie/')

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
            request.session['potwierdzenie'] = \
                'Certyfikat został poprawnie dodany.'
            return redirect('/komunikat/potwierdzenie/')

    else:
        formularz = Formularz_Certyfikat()

    return render(request, 'produkt/dodaj.html',
                            {'formularz': formularz})




def Dodaj_Polecane(request):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':
        formularz = Formularz_Polecane(request.POST)

        if formularz.is_valid():
            formularz.save()
            request.session['potwierdzenie'] = \
                'Nowy produkt został poprawnie dodany do ' \
                'listy produktów polecanych.'
            return redirect('/komunikat/potwierdzenie/')

    else:
        formularz = Formularz_Polecane()

    return render(request, 'produkt/dodaj.html',
                            {'formularz': formularz})




################## Usuwanie ##################

def Usun_Produkt(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    produkt = Produkt.objects.get(id=pk)
    meta_tag = Meta_Tagi.objects.get(
        adres_strony='/produkt/%s/' % str(produkt.pk))

    produkt.delete()
    meta_tag.delete()
    return redirect('/edytuj/')




def Usun_Producent(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    Producent.objects.get(id=pk).delete()
    return redirect('/edytuj/')




def Usun_Kolor(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    Kolor.objects.get(id=pk).delete()
    return redirect('/edytuj/')




def Usun_Certyfikat(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    Certyfikat.objects.get(id=pk).delete()
    return redirect('/edytuj/')




def Usun_Polecane(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    Polecane.objects.get(id=pk).delete()
    return redirect('/edytuj/')




################## Edycja ##################

def Edytuj_Produkt(request, pk):
    Sprawdz_Czy_Zalogowany(request)
    produkt = get_object_or_404(Produkt, id=pk)

    if request.method == 'POST':
        formularz = Formularz_Produktu(request.POST, request.FILES,
                                       instance=produkt)

        if formularz.is_valid():
            produkt = formularz.save()
            produkt.save()

                # metatagi
            meta_tag = Meta_Tagi.objects.get(pk='/produkt/%s/' % str(pk))
            meta_tag.description = produkt.opis[0:154]
            meta_tag.og_image = str(produkt.zdjecie)
            meta_tag.save()

            Zarzadzaj_Zdjeciem_Produktu(produkt, formularz)
            return redirect('/edytuj/')

    else:
        formularz = Formularz_Produktu(instance=produkt)

    return render(request, 'produkt/edytuj.html',
                            {'formularz': formularz})




def Edytuj_Polecane(request, pk):
    Sprawdz_Czy_Zalogowany(request)

    if request.method == 'POST':

            # edycja POSTa
        dane_form = request.POST.copy()
        dane_form['produkt'] = str(pk)

        polecany = Polecane.objects.get(id=pk)
        formularz = Formularz_Polecane(data=dane_form,
                                       instance=polecany)

        if formularz.is_valid():
            formularz.save()

    return redirect('Wyswietl_Edytuj')




################## Pobieranie ##################

def Pobierz_Szczegoly_Produktu(request, pk):
    produkt = Produkt.objects.get(id=pk)
    return render(request, 'produkt/szczegoly.html',
                            {'produkt': produkt})




################## Dodatki ##################

def Zarzadzaj_Zdjeciem_Produktu(produkt, formularz):

    if formularz.cleaned_data['zewnetrzny_url']:
        produkt.Zapisz_Zdjecie_URL(formularz.cleaned_data['zewnetrzny_url'])

    if formularz.cleaned_data['zdjecie']:
        if '/static/img/produkt/' not in str(formularz.cleaned_data['zdjecie']):
            produkt.Zapisz_Zdjecie_Formularz()
