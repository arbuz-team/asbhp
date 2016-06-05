# -*- coding: utf-8 -*-
from django.shortcuts import render
from produkt.models import *
from forms import *

################## Zakładki ##################

def Start(request):
    polecane = Polecane.objects.all()
    return render(request, 'asbhp/start.html', {'polecane': polecane})


def O_Firmie(request):
    css_menu = ['wybrany', '', '']
    return render(request, 'asbhp/o_firmie.html', {'css_menu': css_menu})


def Oferta(request):
    css_menu = ['', 'wybrany', '']
    typ = Typ_Odziezy.objects.all()
    dziedzina = Dziedzina_Odziezy.objects.all()
    rodzaj = Rodzaj_Odziezy.objects.all()
    return render(request, 'asbhp/oferta.html', {'css_menu': css_menu,
                                                 'typ': typ,
                                                 'dziedzina': dziedzina,
                                                 'rodzaj': rodzaj})


def Kontakt(request):
    css_menu = ['', '', 'wybrany']
    return render(request, 'asbhp/kontakt.html', {'css_menu': css_menu})

