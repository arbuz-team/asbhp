# -*- coding: utf-8 -*-
from django.forms.extras.widgets import SelectDateWidget
from django import forms
from models import *
import imghdr

class Formularz_Produktu(forms.ModelForm):

    zewnetrzny_url = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Wklej adres url zdjęcia'}))

    def __init__(self, *args, **kwargs):
        super(Formularz_Produktu, self).__init__(*args, **kwargs)

        self.fields['producent'].empty_label = 'Wybierz firmę...'
        self.fields['kolor'].empty_label = 'Wybierz kolor...'
        self.fields['rodzaj'].empty_label = 'Wybierz rodzaj odzieży...'

    def clean_zewnetrzny_url(self):
        zewnetrzny_url = self.cleaned_data['zewnetrzny_url']
        if zewnetrzny_url:
            plik = cStringIO.StringIO(urllib.urlopen(zewnetrzny_url).read())
            if not imghdr.what(plik):
                raise forms.ValidationError('To przecież nie jest obrazek!')

        return zewnetrzny_url

    class Meta:
        model = Produkt
        fields = ('nazwa', 'opis', 'slowa_kluczowe', 'rozmiar',
                  'producent', 'kolor', 'rodzaj', 'certyfikaty',
                  'zagrozenia', 'zawody', 'zdjecie', 'zewnetrzny_url')

        widgets = {
            'nazwa':    forms.TextInput(attrs={'placeholder': 'Wpisz nazwę'}),
            'opis':     forms.Textarea(attrs={'placeholder': 'Wpisz opis'}),
            'slowa_kluczowe': forms.Textarea(attrs={'placeholder': 'Wpisz słowa kluczowe'}),
            'rozmiar':  forms.TextInput(attrs={'placeholder': 'Wpisz rozmiar'}),
        }

        error_messages = {
            'nazwa': {'required': 'Co to za produkt, bez nazwy...'},
            'opis': {'required': 'Ludzie chcą wiedzieć, co kupują.'},
            'producent': {'required': 'Minimum, potrzebne do filtrowania.'},
            'kolor': {'required': 'Minimum, potrzebne do filtrowania.'},
            'rodzaj': {'required': 'Minimum, potrzebne do filtrowania.'},
            'zdjecie': {'invalid_image': 'To przecież nie jest obrazek!'}
        }

class Formularz_Promowania(forms.ModelForm):

    class Meta:
        model = Polecane
        fields = ('produkt', 'data_zakonczenia')


class Formularz_Producent(forms.ModelForm):

    class Meta:
        model = Producent
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
        fields = ('opis', 'rodzaj', 'producent')


class Formularz_Polecane(forms.ModelForm):

    data_zakonczenia = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = Polecane
        fields = ('produkt', 'data_zakonczenia')
