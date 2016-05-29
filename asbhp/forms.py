# -*- coding: utf-8 -*-
from django import forms
from models import *

class Formularz_Produktu(forms.ModelForm):

        # certyfikaty
    cn1 = forms.CharField(label='', max_length=20)
    cn2 = forms.CharField(label='', max_length=20)
    cn3 = forms.CharField(label='', max_length=20)
    cn4 = forms.CharField(label='', max_length=20)
    cn5 = forms.CharField(label='', max_length=20)

    cs1 = forms.CharField(label='', max_length=50)
    cs2 = forms.CharField(label='', max_length=50)
    cs3 = forms.CharField(label='', max_length=50)
    cs4 = forms.CharField(label='', max_length=50)
    cs5 = forms.CharField(label='', max_length=50)

        # zagrożenia
    zgn1 = forms.CharField(label='', max_length=50)
    zgn2 = forms.CharField(label='', max_length=50)
    zgn3 = forms.CharField(label='', max_length=50)
    zgn4 = forms.CharField(label='', max_length=50)
    zgn5 = forms.CharField(label='', max_length=50)

        # zawody
    zwn1 = forms.CharField(label='', max_length=50)
    zwn2 = forms.CharField(label='', max_length=50)
    zwn3 = forms.CharField(label='', max_length=50)
    zwn4 = forms.CharField(label='', max_length=50)
    zwn5 = forms.CharField(label='', max_length=50)

    class Meta:
        model = Produkt
        fields = ('nazwa', 'opis', 'firma', 'kolor',
                  'rozmiar', 'waga', 'sztuk', 'rodzaj',
                  'cn1', 'cs1', 'cn2', 'cs2', 'cn3', 'cs3',
                  'cn4', 'cs4', 'cn5', 'cs5',
                  'zgn1', 'zgn2', 'zgn3', 'zgn4', 'zgn5',
                  'zwn1', 'zwn2', 'zwn3', 'zwn4', 'zwn5')


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

