# -*- coding: utf-8 -*-
from django import forms
from dodatek.views import *
from models import *

class Formularz_Logowania(forms.Form):

    login = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Login'}))

    haslo = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))

    def clean_login(self):
        login = self.cleaned_data['login']
        if not Uzytkownicy.objects.filter(login=login):
            raise forms.ValidationError('Użytkownik o podanym loginie'
                                        'nie istnieje.')
        return login

    def clean_haslo(self):
        login = self.cleaned_data['login']
        haslo = self.cleaned_data['haslo']
        uzytkownik = Uzytkownicy.objects.get(login=login)
        if uzytkownik.haslo != Szyfruj(haslo):
            raise forms.ValidationError('Błędne hasło. '
                                        'Spróbuj jeszcze raz.')
        return haslo


class Formularz_Rejestracji(forms.ModelForm):

    def clean_haslo(self):
        return Szyfruj(self.cleaned_data['haslo'])

    class Meta:
        model = Uzytkownicy
        fields = ('login', 'haslo')

        widgets = {
            'login': forms.TextInput(attrs={'placeholder': 'Login'}),
            'haslo': forms.PasswordInput(attrs={'placeholder': 'Hasło'}),
        }