from django.shortcuts import render

def Wyswietl_404(request):
    return render(request, 'komunikat/404.html', {})

