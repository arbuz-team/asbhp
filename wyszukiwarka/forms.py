# -*- coding: utf-8 -*-
from django import forms
from models import *

class Formularz_Wyszukiwarki(forms.Form):

    zapytanie = forms.CharField(label='')
    liczba_wyswietlanych_produktow = forms.ChoiceField(choices=(
        (4, 4),
        (8, 8),
        (12, 12),
        (16, 16),
        (20, 20),
    ))

    def clean_zapytanie(self):
        zapytanie = self.cleaned_data['zapytanie']
        if len(zapytanie) < 3:
            raise forms.ValidationError('Wyszukiwana fraza musi '
                                        'zawierać minimum 3 znaki.')

        return zapytanie
