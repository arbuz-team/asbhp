# -*- coding: utf-8 -*-
from django import forms

class Formularz_Wyszukiwarki(forms.Form):

    zapytanie = forms.CharField(label='')

    def clean_zapytanie(self):
        zapytanie = self.cleaned_data['zapytanie']
        if len(zapytanie) < 3:
            raise forms.ValidationError('Wyszukiwana fraza musi '
                                        'zawierać minimum 3 znaki.')

        return zapytanie
