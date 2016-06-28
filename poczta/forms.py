# -*- coding: utf-8 -*-
from django import forms




class Formularz_Wybierz_Temat(forms.Form):
    temat = forms.ChoiceField\
    (
        choices=
        (
            (None, 'Wybierz temat wiadomości'),
            (1, 'Pytanie o dostępność produktu'),
            (2, 'Uwagi dotyczące strony www'),
            (3, 'Inny temat'),
        )
    )




class Formularz_Pytanie_O_Produkt(forms.Form):

    nadawca = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Wpisz nadawcę'}))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Wpisz email'}))

    produkt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Wpisz nazwę produktu'}))

    wiadomosc = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 'none', 'cols': 'none',
               'placeholder': 'Wpisz treść wiadomości'}))




class Formularz_Uwagi_WWW(forms.Form):

    nadawca = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Wpisz nadawcę'}))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Wpisz email'}))

    url = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Wpisz adres strony'}))

    wiadomosc = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 'none', 'cols': 'none',
               'placeholder': 'Wpisz treść wiadomości'}))




class Formularz_Inny_Temat(forms.Form):

    nadawca = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Wpisz nadawcę'}))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Wpisz email'}))

    wiadomosc = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 'none', 'cols': 'none',
               'placeholder': 'Wpisz treść wiadomości'}))
