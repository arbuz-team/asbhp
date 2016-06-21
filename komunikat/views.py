from django.shortcuts import render


def Wyswietl_404(request):
    return render(request, 'komunikat/404.html', {})


def Wyswietl_Email_Wyslany(request):
    return render(request, 'komunikat/email_wyslany.html, {}')
