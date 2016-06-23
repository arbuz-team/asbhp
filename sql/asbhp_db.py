# -*- coding: utf-8 -*-
from asbhp.models import *
from produkt.models import *

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

################## Meta Tagi ##################

Meta_Tagi.objects.create(
    adres_strony='/produkt/1/',
    description=Produkt.objects.get(pk=1).opis[0:154],
    og_type='produkt',
    og_url='http://asbhp.arbuz.team/produkt/1/',
    og_image=str(Produkt.objects.get(pk=1).zdjecie)
).save()


Meta_Tagi.objects.create(
    adres_strony='/produkt/2/',
    description=Produkt.objects.get(pk=2).opis[0:154],
    og_type='produkt',
    og_url='http://asbhp.arbuz.team/produkt/2/',
    og_image=str(Produkt.objects.get(pk=2).zdjecie)
).save()

Meta_Tagi.objects.create(
    adres_strony='/produkt/3/',
    description=Produkt.objects.get(pk=3).opis[0:154],
    og_type='produkt',
    og_url='http://asbhp.arbuz.team/produkt/3/',
    og_image=str(Produkt.objects.get(pk=3).zdjecie)
).save()

Meta_Tagi.objects.create(
    adres_strony='/produkt/4/',
    description=Produkt.objects.get(pk=4).opis[0:154],
    og_type='produkt',
    og_url='http://asbhp.arbuz.team/produkt/4/',
    og_image=str(Produkt.objects.get(pk=4).zdjecie)
).save()

Meta_Tagi.objects.create(
    adres_strony='/produkt/5/',
    description=Produkt.objects.get(pk=5).opis[0:154],
    og_type='produkt',
    og_url='http://asbhp.arbuz.team/produkt/5/',
    og_image=str(Produkt.objects.get(pk=5).zdjecie)
).save()

Meta_Tagi.objects.create(
    adres_strony='/produkt/6/',
    description=Produkt.objects.get(pk=6).opis[0:154],
    og_type='produkt',
    og_url='http://asbhp.arbuz.team/produkt/6/',
    og_image=str(Produkt.objects.get(pk=6).zdjecie)
).save()

Meta_Tagi.objects.create(
    adres_strony='/produkt/7/',
    description=Produkt.objects.get(pk=7).opis[0:154],
    og_type='produkt',
    og_url='http://asbhp.arbuz.team/produkt/7/',
    og_image=str(Produkt.objects.get(pk=7).zdjecie)
).save()

Meta_Tagi.objects.create(
    adres_strony='/produkt/8/',
    description=Produkt.objects.get(pk=8).opis[0:154],
    og_type='produkt',
    og_url='http://asbhp.arbuz.team/produkt/8/',
    og_image=str(Produkt.objects.get(pk=8).zdjecie)
).save()

Meta_Tagi.objects.create(
    adres_strony='/produkt/9/',
    description=Produkt.objects.get(pk=9).opis[0:154],
    og_type='produkt',
    og_url='http://asbhp.arbuz.team/produkt/9/',
    og_image=str(Produkt.objects.get(pk=9).zdjecie)
).save()

Meta_Tagi.objects.create(
    adres_strony='/produkt/10/',
    description=Produkt.objects.get(pk=10).opis[0:154],
    og_type='produkt',
    og_url='http://asbhp.arbuz.team/produkt/10/',
    og_image=str(Produkt.objects.get(pk=10).zdjecie)
).save()





Meta_Tagi.objects.create(
    adres_strony='/',
    description='Strona startowa',
    og_type='Start',
    og_url='http://asbhp.arbuz.team/',
    og_image='/static/img/AS_C,S.png'
).save()

Meta_Tagi.objects.create(
    adres_strony='/o_firmie/',
    description='Firma Handlowa "AS BHP"',
    og_type='O Firmie',
    og_url='http://asbhp.arbuz.team/o_firmie/',
    og_image='/static/img/AS_C,S.png'
).save()

Meta_Tagi.objects.create(
    adres_strony='/oferta/',
    description='Nasze produkty',
    og_type='Oferta',
    og_url='http://asbhp.arbuz.team/oferta/',
    og_image='/static/img/AS_C,S.png'
).save()

Meta_Tagi.objects.create(
    adres_strony='/kontakt/',
    description='Firma Handlowa "AS BHP"',
    og_type='Kontakt',
    og_url='http://asbhp.arbuz.team/kontakt/',
    og_image='/static/img/AS_C,S.png'
).save()

