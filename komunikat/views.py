from django.shortcuts import render

def Wyswietl_404(request, komunikat):
    return render(request, 'komunikat/404.html', {'komunikat': komunikat})

