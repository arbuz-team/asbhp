# -*- coding: utf-8 -*-
from django import forms
from produkt.models import *

class Formularz_Wyszukiwarki(forms.Form):

    zapytanie = forms.CharField(label='')
    '''liczba_wyswietlanych_produktow = forms.ChoiceField(choices=(
        (4, 4),
        (8, 8),
        (12, 12),
        (16, 16),
        (20, 20),
    ))'''

    def clean_zapytanie(self):
        zapytanie = self.cleaned_data['zapytanie']
        if len(zapytanie) < 3:
            raise forms.ValidationError('Wyszukiwana fraza musi '
                                        'zawierać minimum 3 znaki.')
        return zapytanie

    def Ustaw_Zapytanie(self, wartosc):
        self.fields['zapytanie'].initial = wartosc


class Formularz_Filtru_Producent(forms.ModelForm):

    class Meta:
        model = Produkt
        fields = ('producent',)


class Formularz_Filtru_Kolor(forms.ModelForm):

    class Meta:
        model = Produkt
        fields = ('kolor',)


class Formularz_Filtru_Zagrozenia(forms.ModelForm):

    class Meta:
        model = Produkt
        fields = ('zagrozenia',)


class Formularz_Filtru_Zawody(forms.ModelForm):

    class Meta:
        model = Produkt
        fields = ('zawody',)


class Formularz_Kontener(forms.Form):
    zawartosc = forms.CharField()
