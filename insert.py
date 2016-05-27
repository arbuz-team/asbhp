# -*- coding: utf-8 -*-
from models import *

Typ_Odziezy.objects.create(nazwa='Ochrona głowy').save()

Dziedzina_Odziezy.objects.create(nazwa='Ochrona wzroku', id_typ=Typ_Odziezy.objects.get(nazwa='Ochrona głowy')).save()
Dziedzina_Odziezy.objects.create(nazwa='Ochrona czaszki', id_typ=Typ_Odziezy.objects.get(nazwa='Ochrona głowy')).save()
Dziedzina_Odziezy.objects.create(nazwa='Ochrona słuchu', id_typ=Typ_Odziezy.objects.get(nazwa='Ochrona głowy')).save()
Dziedzina_Odziezy.objects.create(nazwa='Ochrona dróg oddechowych', id_typ=Typ_Odziezy.objects.get(nazwa='Ochrona głowy')).save()

Rodzaj_Odziezy.objects.create(nazwa='Okulary ochronne', id_dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona wzroku')).save()
Rodzaj_Odziezy.objects.create(nazwa='Gogle ochronne', id_dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona wzroku')).save()
Rodzaj_Odziezy.objects.create(nazwa='Przyłbice spawalnicze', id_dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona wzroku')).save()
Rodzaj_Odziezy.objects.create(nazwa='Osłony ochronne', id_dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona wzroku')).save()

Rodzaj_Odziezy.objects.create(nazwa='Hełmy ochronne', id_dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona czaszki')).save()
Rodzaj_Odziezy.objects.create(nazwa='Hełmy lekkie', id_dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona czaszki')).save()

Rodzaj_Odziezy.objects.create(nazwa='Nauszniki przeciwhałasowe', id_dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona słuchu')).save()
Rodzaj_Odziezy.objects.create(nazwa='Wkładki przeciwhałasowe', id_dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona słuchu')).save()

Rodzaj_Odziezy.objects.create(nazwa='Maski jednorazowe', id_dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona dróg oddechowych')).save()
Rodzaj_Odziezy.objects.create(nazwa='Maski wielokrotnego użytku', id_dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona dróg oddechowych')).save()
