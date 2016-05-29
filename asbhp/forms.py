# -*- coding: utf-8 -*-
from django import forms
from models import *

class Formularz_Produktu(forms.ModelForm):

        # certyfikaty
    cn1 = forms.CharField(max_length=20)
    cn2 = forms.CharField(max_length=20)
    cn3 = forms.CharField(max_length=20)
    cn4 = forms.CharField(max_length=20)
    cn5 = forms.CharField(max_length=20)

    cs1 = forms.CharField(max_length=20)
    cs2 = forms.CharField(max_length=20)
    cs3 = forms.CharField(max_length=20)
    cs4 = forms.CharField(max_length=20)
    cs5 = forms.CharField(max_length=20)

        # zagrożenia
    zn1 = forms.CharField(max_length=20)
    zn2 = forms.CharField(max_length=20)
    zn3 = forms.CharField(max_length=20)
    zn4 = forms.CharField(max_length=20)
    zn5 = forms.CharField(max_length=20)

        # zawody
    zn = forms.CharField(max_length=20)

    class Meta:
        model = Produkt
        fields = ('nazwa', 'opis', 'firma', 'kolor',
                  'rozmiar', 'waga', 'sztuk', 'rodzaj')


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

