# -*- coding: utf-8 -*-
from django import forms
from produkt.models import *



class Formularz_Wyszukiwarki(forms.Form):

    zapytanie = forms.CharField\
    (
        label='',
        error_messages={'required': ''},
        widget=forms.TextInput(attrs={'class': 'focus'})
    )


    def clean_zapytanie(self):
        zapytanie = self.cleaned_data['zapytanie']

        if len(zapytanie) < 3:
            raise forms.ValidationError('Wyszukiwana fraza musi '
                                        'zawierać minimum 3 znaki.')
        return zapytanie




class Formularz_Filtru_Producent(forms.Form):

    producent = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'focus'}))


    def Ustaw_Pola(self, produkt):

            # wyświetla wszystkie firmy, gdy produktów za dużo
        wybor = {(p.id, str(p)) for p in Producent.objects.all()}
        if len(produkt) < 100:
            wybor = {(p.producent.id, str(p.producent)) for p in produkt}

        wybor.add((0, 'Wszystkie'))
        wybor = sorted(wybor)
        self.fields['producent'].choices = wybor


    def Waliduj(self):
        if 'producent' in self.data:
            return True if self.data['producent'] else False

        return False


    def Pobierz_Wybrany(self):
        return self.data['producent'] \
            if self.Waliduj() else None




class Formularz_Filtru_Kolor(forms.Form):

    kolor = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'focus'}))


    def Ustaw_Pola(self, produkt):

            # nie wyświetla kolorów, gdy produktów za dużo
        wybor = {(0, 'Wszystkie')}
        if len(produkt) < 100:
            wybor = {(p.kolor.id, str(p.kolor)) for p in produkt}
            wybor.add((0, 'Wszystkie'))

        wybor = sorted(wybor)
        self.fields['kolor'].choices = wybor



    def Waliduj(self):
        if 'kolor' in self.data:
            return True if self.data['kolor'] else False

        return False


    def Pobierz_Wybrany(self):
        return self.data['kolor'] \
            if self.Waliduj() else None




class Formularz_Filtru_Zagrozenia(forms.ModelForm):

    class Meta:
        model = Produkt
        fields = ('zagrozenia',)
        widgets = {'zagrozenia': forms.SelectMultiple(
                    attrs={'class': 'focus'})}




class Formularz_Filtru_Zawody(forms.ModelForm):

    class Meta:
        model = Produkt
        fields = ('zawody',)
        widgets = {'zawody': forms.SelectMultiple(
                    attrs={'class': 'focus'})}




class Formularz_Filtru_Liczba_Produktow(forms.Form):

    liczba = forms.ChoiceField\
    (
        choices=
        (
            (1, 1),
            (2, 2),
            (4, 4),
            (8, 8),
            (12, 12),
            (16, 16),
            (20, 20),
        ),
        initial=8,
        widget=forms.Select(attrs={'class': 'focus'})
    )




class Formularz_Kontener(forms.Form):
    zawartosc = forms.CharField()
