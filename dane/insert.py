# -*- coding: utf-8 -*-
from asbhp.models import *

################## Opis ##################
Opis.objects.create(numer=1, opis='Okulary z poliwęglanu. Sportowy wygląd. Nylonowa matowa oprawka dla większej wygody i trwałości.').save()

################## Firma ##################
Firma.objects.create(nazwa='Kilauea').save()

################## Kolor ##################
Kolor.objects.create(nazwa='Polaryzacyjne').save()
Kolor.objects.create(nazwa='Odblaskowy').save()
Kolor.objects.create(nazwa='Bezbarwny').save()

################## Certyfikat ##################
Certyfikat.objects.create(numer='EN166', szczegoly='1 FT/FT').save()
Certyfikat.objects.create(numer='EN172', szczegoly='UV 5-3.1').save()
Certyfikat.objects.create(numer='EN170', szczegoly='UV 2C-1.2').save()

################## Zagrożenie ##################
Zagrozenie.objects.create(nazwa='Antyelektrostatyczność').save()
Zagrozenie.objects.create(nazwa='Hałas').save()
Zagrozenie.objects.create(nazwa='Ciepło').save()
Zagrozenie.objects.create(nazwa='Uderzenie').save()
Zagrozenie.objects.create(nazwa='Upadek').save()
Zagrozenie.objects.create(nazwa='Przecięcie/Przekłucie').save()
Zagrozenie.objects.create(nazwa='Zimno/Niepogoda').save()
Zagrozenie.objects.create(nazwa='Poślizg').save()
Zagrozenie.objects.create(nazwa='Cząsteczki biologiczne, chemiczne').save()
Zagrozenie.objects.create(nazwa='Zużycie').save()
Zagrozenie.objects.create(nazwa='UV/IR').save()
Zagrozenie.objects.create(nazwa='Elektryczność').save()
Zagrozenie.objects.create(nazwa='Słaba widoczność').save()

################## Zawód ##################
Zawod.objects.create(nazwa='Rolnictwo/ogrodnictwo').save()
Zawod.objects.create(nazwa='Budownictwo i roboty publiczne').save()
Zawod.objects.create(nazwa='Prace remontowe/rzemiosło').save()
Zawod.objects.create(nazwa='Przemysł ciężki').save()
Zawod.objects.create(nazwa='Przemysł lekki').save()
Zawod.objects.create(nazwa='Usługi/logistyka').save()
Zawod.objects.create(nazwa='Służba zdrowia/żywienie zbiorowe').save()
Zawod.objects.create(nazwa='Przemysł petrochemiczny/gazowniczy').save()
Zawod.objects.create(nazwa='Górnictwo').save()
Zawod.objects.create(nazwa='Energia wiatrowa').save()

################## Ochrona głowy: Kontenery ##################
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

################## Ochrona głowy: Produkty ##################
Produkt.objects.create(nazwa='Kilauea polarised',
                       opis=Opis.objects.get(numer=1),
                       firma=Firma.objects.get(nazwa='Kilauea'),
                       kolor=Kolor.objects.get(nazwa='Polaryzacyjne'),
                       waga=28,
                       sztuk=100,
                       id_rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Okulary ochronne')
                       ).save()

Produkt.objects.create(nazwa='Kilauea mirror',
                       opis=Opis.objects.get(numer=1),
                       firma=Firma.objects.get(nazwa='Kilauea'),
                       kolor=Kolor.objects.get(nazwa='Odblaskowy'),
                       waga=28,
                       sztuk=100,
                       id_rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Okulary ochronne')
                       ).save()

Produkt.objects.create(nazwa='Kilauea clear',
                       opis=Opis.objects.get(numer=1),
                       firma=Firma.objects.get(nazwa='Kilauea'),
                       kolor=Kolor.objects.get(nazwa='Bezbarwny'),
                       waga=28,
                       sztuk=100,
                       id_rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Okulary ochronne')
                       ).save()

################## Dodatek ##################
