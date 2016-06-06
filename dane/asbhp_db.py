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
