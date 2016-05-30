# -*- coding: utf-8 -*-
from django import forms
from models import *

class Formularz_Produktu(forms.ModelForm):

    def __init__(self, auto_id):
        super(Formularz_Produktu, self).__init__(auto_id)

        self.fields['firma'].empty_label = 'Wybierz firmę...'
        self.fields['kolor'].empty_label = 'Wybierz kolor...'
        self.fields['rodzaj'].empty_label = 'Wybierz rodzaj odzieży...'

    class Meta:
        model = Produkt
        fields = ('nazwa', 'opis', 'firma', 'kolor',
                  'rozmiar', 'waga', 'sztuk', 'rodzaj',
                  'certyfikaty', 'zagrozenia', 'zawody')

        widgets = {
            'nazwa':    forms.TextInput(attrs={'placeholder': 'Wpisz nazwę'}),
            'opis':     forms.Textarea(attrs={'placeholder': 'Wpisz opis'}),
            'rozmiar':  forms.TextInput(attrs={'placeholder': 'Wpisz rozmiar'}),
            'waga':     forms.NumberInput(attrs={'placeholder': 'Wpisz wagę (g)'}),
            'sztuk':    forms.NumberInput(attrs={'placeholder': 'Wpisz sztuk/opak'}),
        }


class Formularz_Promowania(forms.ModelForm):

    class Meta:
        model = Polecane
        fields = ('produkt', 'data_zakonczenia')


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

