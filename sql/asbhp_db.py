# -*- coding: utf-8 -*-
from asbhp.models import *

Kontakt.objects.create(zawartosc='F.H. "AS BHP"', przeznaczenie='tytul').save()
Kontakt.objects.create(zawartosc='ul. Hutnicza 34\n'
                                 '81-061 Gdynia\n'
                                 'tel./fax (058) 667-30-05\n'
                                 'NIP: 584-118-58-16\n'
                                 'e-mail: asbhp@asbhp.pl', przeznaczenie='tekst').save()
Kontakt.objects.create(zawartosc='<iframe src="https://www.google.com/'
                                 'maps/embed?pb=!1m18!1m12!1m3!1d23329.'
                                 '037923675103!2d18.449952872488762!3d54.'
                                 '541716876913796!2m3!1f0!2f0!3f0!3m2!'
                                 '1i1024!2i768!4f13.1!3m3!1m2!1s0x46fda4253c82111b'
                                 '%3A0x6bef0ffaf6dc0ea2!2sAS+BHP!5e0!3m2!1spl!'
                                 '2spl!4v1466025172930" width="100%" height="100%" '
                                 'frameborder="0" style="border:0" '
                                 'allowfullscreen></iframe>', przeznaczenie='mapa').save()

O_Firmie.objects.create(zawartosc='Firma Handlowa "AS BHP"', przeznaczenie='tytul').save()
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
                        przeznaczenie='tekst').save()

