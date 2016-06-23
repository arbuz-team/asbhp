from django.shortcuts import render


def Wyswietl_404(request):
    return render(request, 'komunikat/404.html', {})


def Wyswietl_Potwierdzenie(request):
    return render(request, 'komunikat/potwierdzenie.html', {})