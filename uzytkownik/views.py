from forms import *

def Logowanie(request):

    if request.method == 'POST':
        formularz = Formularz_Logowania(request.POST)

        if formularz.is_valid():
            request.session['zalogowany'] = True
            return redirect('Wyswietl_Start')

    else:
        formularz = Formularz_Logowania()

    return render(request, 'uzytkownik/logowanie.html',
                            {'formularz': formularz})


def Rejestracja(request):

    if request.method == 'POST':
        formularz = Formularz_Rejestracji(request.POST)

        if formularz.is_valid():
            formularz.save()
            return redirect('Wyswietl_Start')

    else:
        formularz = Formularz_Rejestracji()

    return render(request, 'uzytkownik/rejestracja.html',
                            {'formularz': formularz})


def Wyloguj(request):
    request.session['zalogowany'] = False
    return redirect('Wyswietl_Start')
