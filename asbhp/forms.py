# -*- coding: utf-8 -*-
from django import forms
from models import *

class Formularz_Produktu(forms.ModelForm):



    class Meta:
        model = Produkt
        fields = ('nazwa', 'opis', 'firma', 'kolor',
                  'rozmiar', 'waga', 'sztuk', 'rodzaj',
                  'certyfikaty', 'zagrozenia', 'zawody')


class Formularz_Promowania(forms.ModelForm):

    class Meta:
        model = Polecane
        fields = ('produkt', 'data_zakonczenia')


class Formularz_Opis(forms.ModelForm):

    class Meta:
        model = Opis
        fields = ('opis',)


class Formularz_Firma(forms.ModelForm):

    class Meta:
        model = Firma
        fields = ('nazwa',)


class Formularz_Kolor(forms.ModelForm):

    class Meta:
        model = Kolor
        fields = ('nazwa',)


class Formularz_Certyfikat(forms.ModelForm):

    class Meta:
        model = Certyfikat
        fields = ('numer', 'szczegoly')


class Formularz_Dodatek(forms.ModelForm):

    class Meta:
        model = Dodatek
        fields = ('opis', 'rodzaj', 'firma')


class Formularz_Polecane(forms.ModelForm):

    class Meta:
        model = Polecane
        fields = ('produkt', 'data_zakonczenia')


#class Formularz_Zakladki(forms.ModelForm):
#
#    class Meta:
#        model = Zakladka
#        fields = ('nazwa', 'zawartosc')
#
##        widgets = {
##            'nazwa': forms.TextInput(attrs={'class' : 'papapa'}),
##        }
#

