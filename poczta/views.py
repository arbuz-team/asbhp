# -*- coding: utf-8 -*-
from dodatek.views import *
from forms import *
from django.core.mail import EmailMessage



def Wyslij_Email(request, wiadomosc, nadawca_email):

    email = EmailMessage(
        Pobierz_Temat(request),
        wiadomosc,
        nadawca_email,
        ['kontakt.arbuz.team@gmail.com']
        #headers={'Reply-To': '93.endo@gmail.com'}
    )

    email.send()
    request.session['wybrany_temat'] = ''




def Ustaw_Fromularz_Email(request):

        # Pytanie o dostępność produktu
    if request.session['wybrany_temat'] == '1':
        request.session['poczta_url'] = '/poczta/pytanie_o_produkt/'

        if not request.session['formularz_poczta']:
            request.session['formularz_poczta'] = \
                Formularz_Pytanie_O_Produkt()

        return

        # Uwagi dotyczące strony www
    if request.session['wybrany_temat'] == '2':
        request.session['poczta_url'] = '/poczta/uwagi_www/'

        if not request.session['formularz_poczta']:
            request.session['formularz_poczta'] = \
                Formularz_Uwagi_WWW()

        return

        # Inny temat
    if request.session['wybrany_temat'] == '3':
        request.session['poczta_url'] = '/poczta/inny_temat/'

        if not request.session['formularz_poczta']:
            request.session['formularz_poczta'] = \
                Formularz_Inny_Temat()

        return

        # formularz startowy
    request.session['poczta_url'] = '/poczta/wybierz_temat/'
    if not request.session['formularz_poczta']:
        request.session['formularz_poczta'] = \
            Formularz_Wybierz_Temat()




def Pobierz_Temat(request):
    return {'1': 'Pytanie o dostępność produktu',
            '2': 'Uwagi dotyczące strony www',
            '3': 'Inny temat'}.get(request.session['wybrany_temat'])




################## Odbiór formularzy ##################

def Wybierz_Temat(request):

    if request.method == 'POST':
        formularz = Formularz_Wybierz_Temat(request.POST)

        if formularz.is_valid():
            request.session['wybrany_temat'] = \
                formularz.cleaned_data['temat']

    del request.session['formularz_poczta']
    return redirect('Wyswietl_Kontakt')




def Pytanie_O_Produkt(request):

    if request.method == 'POST':
        formularz = Formularz_Pytanie_O_Produkt(request.POST)

        if formularz.is_valid():
            nadawca = formularz.cleaned_data['nadawca']
            email = formularz.cleaned_data['email']
            produkt = formularz.cleaned_data['produkt']
            wiadomosc = formularz.cleaned_data['wiadomosc']

            wiadomosc += u'\n\nSzczegóły:\n' \
                 '\tNadawca:\t\t'   + nadawca   + '\n' + \
                 '\tEmail:\t\t'     + email     + '\n' + \
                 '\tProdukt:\t\t'   + produkt

            Wyslij_Email(request, wiadomosc, email)
            request.session['potwierdzenie'] = \
                'Email został wysłany.'
            return redirect('/komunikat/potwierdzenie/')

            # zapisanie formularza do sesji
        request.session['formularz_poczta'] = formularz

    return redirect('Wyswietl_Kontakt')




def Uwagi_WWW(request):

    if request.method == 'POST':
        formularz = Formularz_Uwagi_WWW(request.POST)

        if formularz.is_valid():
            nadawca = formularz.cleaned_data['nadawca']
            email = formularz.cleaned_data['email']
            url = formularz.cleaned_data['url']
            wiadomosc = formularz.cleaned_data['wiadomosc']

            wiadomosc += u'\n\nSzczegóły:\n' \
                         '\tNadawca:\t\t' + nadawca + '\n' + \
                         '\tEmail:\t\t' + email + '\n' + \
                         '\tUrl:\t\t' + url

            Wyslij_Email(request, wiadomosc, email)
            return redirect('Wyswietl_Email_Wyslany')

            # zapisanie formularza do sesji
        request.session['formularz_poczta'] = formularz

    return redirect('Wyswietl_Kontakt')




def Inny_Temat(request):

    if request.method == 'POST':
        formularz = Formularz_Inny_Temat(request.POST)

        if formularz.is_valid():
            nadawca = formularz.cleaned_data['nadawca']
            email = formularz.cleaned_data['email']
            wiadomosc = formularz.cleaned_data['wiadomosc']

            wiadomosc += u'\n\nSzczegóły:\n' \
                         '\tNadawca:\t\t' + nadawca + '\n' + \
                         '\tEmail:\t\t' + email + '\n'

            Wyslij_Email(request, wiadomosc, email)
            return redirect('Wyswietl_Email_Wyslany')

            # zapisanie formularza do sesji
        request.session['formularz_poczta'] = formularz

    return redirect('Wyswietl_Kontakt')
