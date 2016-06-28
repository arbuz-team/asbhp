# -*- coding: utf-8 -*-
from django import forms
from models import *



class Formularz_Zawartosc_Zakladki(forms.ModelForm):

    class Meta:
        model = Zawartosc_Zakladki
        fields = ('tytul', 'tekst')

        widgets = {
            'tekst': forms.Textarea(attrs={'rows': 'none',
                                           'cols': 'none'}),
        }

        error_messages = {
            'tytul':    {'required': 'Pole nie powinno być puste.'},
            'tekst':    {'required': 'Pole nie powinno być puste.'}
        }
