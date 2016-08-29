# -*- coding: utf-8 -*-
from django import forms
from dodatek.views import *
from .models import *



class Formularz_Logowania(forms.Form):

    login = forms.CharField\
    (
        widget=forms.TextInput(attrs={'placeholder': 'Login'}),
        error_messages={'required': 'Wpisz login.'}
    )

    haslo = forms.CharField\
    (
        widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}),
        error_messages = {'required': 'Wpisz hasło.'}
    )


    def clean_login(self):
        login = self.cleaned_data['login']

        if not Uzytkownicy.objects.filter(login=login):
            raise forms.ValidationError('Użytkownik o podanym '
                                        'loginie nie istnieje.')
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

    powtorz_haslo = forms.CharField\
    (
        widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}),
        error_messages = {'required': 'Wpisz hasło jeszcze raz.'}
    )

    def clean_haslo(self):
        return Szyfruj(self.cleaned_data['haslo'])

    def clean_powtorz_haslo(self):
        haslo = self.cleaned_data['haslo']
        powtorz_haslo = self.cleaned_data['powtorz_haslo']

        if haslo != Szyfruj(powtorz_haslo):
            raise forms.ValidationError('Hasła są niezgodne. '
                                        'Spróbuj jeszcze raz.')
        return powtorz_haslo


    class Meta:
        model = Uzytkownicy
        fields = ('login', 'haslo')

        widgets = \
        {
            'login': forms.TextInput(
                attrs={'placeholder': 'Login'}),

            'haslo': forms.PasswordInput(
                attrs={'placeholder': 'Hasło'}),
        }

        error_messages = \
        {
            'login': {'required': 'Wpisz login.'},
            'haslo': {'required': 'Wpisz hasło'},
        }
