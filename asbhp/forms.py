# -*- coding: utf-8 -*-
from django import forms
from models import *

class Formularz_Kontakt(forms.ModelForm):

    class Meta:
        model = Kontakt
        fields = ('zawartosc', 'css')