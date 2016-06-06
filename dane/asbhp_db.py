# -*- coding: utf-8 -*-
from asbhp.models import *

CSS.objects.create(klasa='tytul').save()
CSS.objects.create(klasa='tekst').save()
CSS.objects.create(klasa='zdjecie').save()
CSS.objects.create(klasa='mapa').save()

Kontakt.objects.create(zawartosc='F.H. "AS BHP"', css=CSS.objects.get(klasa='tytul')).save()
Kontakt.objects.create(zawartosc='ul. Hutnicza 34\n'
                                 '81-061 Gdynia\n'
                                 'tel./fax (058) 667-30-05\n'
                                 'NIP: 584-118-58-16\n'
                                 'e-mail: asbhp@asbhp.pl', css=CSS.objects.get(klasa='tekst')).save()
Kontakt.objects.create(zawartosc='(załączona mapa z google)', css=CSS.objects.get(klasa='mapa')).save()

O_Firmie.objects.create(zawartosc='Firma Handlowa AS BHP"', css=CSS.objects.get(klasa='tytul')).save()
O_Firmie.objects.create(zawartosc='Jesteśmy nowoczesną firmą, '
                                  'wykorzystującą najnowsze trendy '
                                  'w konstrukcji ubrań roboczych. '
                                  'Oferujemy również ubrania "tradycyjne" '
                                  '- sprawdzone wielokrotnie w praktyce '
                                  'na różnych stanowiskach pracy. '
                                  'Przedstawicielstwo GRENE, PANOPLY, '
                                  'promo STARS oraz własna produkcja '
                                  'stawia nas w czołówce w branży BHP. '
                                  'Wiele znanych i szanowanych firm '
                                  'należy do grona naszych klientów. '
                                  'Dołącz do nich a przekonasz się jak '
                                  'działamy i co oferujemy. Ubierzemy '
                                  'Twoich pracowników od stóp do głów '
                                  '- również niekonwencjonalnie.',
                        css=CSS.objects.get(klasa='tekst')).save()

