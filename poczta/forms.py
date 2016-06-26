# -*- coding: utf-8 -*-
from django import forms


class Formularz_Wybierz_Temat(forms.Form):
    temat = forms.ChoiceField(
        choices=
        (
            (None, 'Wybierz temat wiadomości'),
            (1, 'Pytanie o dostępność produktu'),
            (2, 'Uwagi dotyczące strony www'),
            (3, 'Inny temat'),
        ))


class Formularz_Pytanie_O_Produkt(forms.Form):
    nadawca = forms.CharField()
    email = forms.EmailField()
    produkt = forms.CharField()
    wiadomosc = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 'none', 'cols': 'none'}))


class Formularz_Uwagi_WWW(forms.Form):
    nadawca = forms.CharField()
    email = forms.EmailField()
    url = forms.URLField()
    wiadomosc = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 'none', 'cols': 'none'}))


class Formularz_Inny_Temat(forms.Form):
    nadawca = forms.CharField()
    email = forms.EmailField()
    wiadomosc = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 'none', 'cols': 'none'}))
