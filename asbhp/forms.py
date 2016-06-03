# -*- coding: utf-8 -*-
from django.forms.extras.widgets import SelectDateWidget
from django import forms
from models import *

class Formularz_Wyszukiwarki(forms.Form):

    zapytanie = forms.CharField(label='')

    def clean_zapytanie(self):
        zapytanie = self.cleaned_data['zapytanie']
        if len(zapytanie) < 3:
            raise forms.ValidationError('Wyszukiwana fraza musi '
                                        'zawierać minimum 3 znaki.')

        return zapytanie


class Formularz_Produktu(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Formularz_Produktu, self).__init__(*args, **kwargs)

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

    data_zakonczenia = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = Polecane
        fields = ('produkt', 'data_zakonczenia')
