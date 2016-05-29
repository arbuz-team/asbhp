from django import forms
from models import *

class Formularz_Promowania(forms.ModelForm):

    class Meta:
        model = Polecane
        fields = ('produkt', 'data_zakonczenia')

class Formularz_Produktu(forms.ModelForm):

    class Meta:
        model = Produkt
        fields = ('nazwa', 'opis', 'firma', 'kolor',
                  'rozmiar', 'waga', 'sztuk', 'rodzaj')

#class Formularz_Zakladki(forms.ModelForm):
#
#    class Meta:
#        model = Zakladka
#        fields = ('nazwa', 'zawartosc')
#
##        widgets = {
##            'nazwa': forms.TextInput(attrs={'class' : 'papapa'}),
##        }
#

