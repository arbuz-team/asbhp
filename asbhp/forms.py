# -*- coding: utf-8 -*-
from django import forms
from models import *

class Formularz_O_Firmie(forms.ModelForm):

    class Meta:
        model = O_Firmie
        fields = ('zawartosc', 'css')

        widgets = {
            'zawartosc': forms.Textarea(attrs={'rows': 'none',
                                               'cols': 'none'}),
        }


class Formularz_Kontakt(forms.ModelForm):

    class Meta:
        model = Kontakt
        fields = ('zawartosc', 'css')

        widgets = {
            'zawartosc': forms.Textarea(attrs={'rows': 'none',
                                               'cols': 'none'}),
        }