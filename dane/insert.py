# -*- coding: utf-8 -*-
from asbhp.models import *
from django.utils import timezone

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

Dziedzina_Odziezy.objects.create(nazwa='Ochrona wzroku', typ=Typ_Odziezy.objects.get(nazwa='Ochrona głowy')).save()
Dziedzina_Odziezy.objects.create(nazwa='Ochrona czaszki', typ=Typ_Odziezy.objects.get(nazwa='Ochrona głowy')).save()
Dziedzina_Odziezy.objects.create(nazwa='Ochrona słuchu', typ=Typ_Odziezy.objects.get(nazwa='Ochrona głowy')).save()
Dziedzina_Odziezy.objects.create(nazwa='Ochrona dróg oddechowych', typ=Typ_Odziezy.objects.get(nazwa='Ochrona głowy')).save()

Rodzaj_Odziezy.objects.create(nazwa='Okulary ochronne', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona wzroku')).save()
Rodzaj_Odziezy.objects.create(nazwa='Gogle ochronne', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona wzroku')).save()
Rodzaj_Odziezy.objects.create(nazwa='Przyłbice spawalnicze', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona wzroku')).save()
Rodzaj_Odziezy.objects.create(nazwa='Osłony ochronne', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona wzroku')).save()

Rodzaj_Odziezy.objects.create(nazwa='Hełmy ochronne', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona czaszki')).save()
Rodzaj_Odziezy.objects.create(nazwa='Hełmy lekkie', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona czaszki')).save()

Rodzaj_Odziezy.objects.create(nazwa='Nauszniki przeciwhałasowe', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona słuchu')).save()
Rodzaj_Odziezy.objects.create(nazwa='Wkładki przeciwhałasowe', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona słuchu')).save()

Rodzaj_Odziezy.objects.create(nazwa='Maski jednorazowe', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona dróg oddechowych')).save()
Rodzaj_Odziezy.objects.create(nazwa='Maski wielokrotnego użytku', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona dróg oddechowych')).save()

################## Ochrona głowy: Produkty ##################
Produkt.objects.create(nazwa='Kilauea polarised',
                       opis=Opis.objects.get(numer=1),
                       firma=Firma.objects.get(nazwa='Kilauea'),
                       kolor=Kolor.objects.get(nazwa='Polaryzacyjne'),
                       waga=28,
                       sztuk=100,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Okulary ochronne')
                       ).save()

Produkt.objects.create(nazwa='Kilauea mirror',
                       opis=Opis.objects.get(numer=1),
                       firma=Firma.objects.get(nazwa='Kilauea'),
                       kolor=Kolor.objects.get(nazwa='Odblaskowy'),
                       waga=28,
                       sztuk=100,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Okulary ochronne')
                       ).save()

Produkt.objects.create(nazwa='Kilauea clear',
                       opis=Opis.objects.get(numer=1),
                       firma=Firma.objects.get(nazwa='Kilauea'),
                       kolor=Kolor.objects.get(nazwa='Bezbarwny'),
                       waga=28,
                       sztuk=100,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Okulary ochronne')
                       ).save()

################## Dodatek ##################
Dodatek.objects.create(numer=1, opis='Nylonowa matowa oprawka dla większej wygody i trwałości', rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Okulary ochronne'), firma=Firma.objects.get(nazwa='Kilauea')).save()
Dodatek.objects.create(numer=2, opis='Z soczewkami polaryzacyjnymi', rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Okulary ochronne'), firma=Firma.objects.get(nazwa='Kilauea')).save()

################## Certyfikaty_Dla_Produktu ##################
Certyfikaty_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea polarised'), certyfikat=Certyfikat.objects.get(numer='EN166')).save()
Certyfikaty_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea mirror'), certyfikat=Certyfikat.objects.get(numer='EN166')).save()
Certyfikaty_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea clear'), certyfikat=Certyfikat.objects.get(numer='EN166')).save()
Certyfikaty_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea polarised'), certyfikat=Certyfikat.objects.get(numer='EN172')).save()
Certyfikaty_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea mirror'), certyfikat=Certyfikat.objects.get(numer='EN172')).save()
Certyfikaty_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea clear'), certyfikat=Certyfikat.objects.get(numer='EN170')).save()

################## Zagrozenia_Dla_Produktu ##################
Zagrozenia_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea polarised'), zagrozenie=Zagrozenie.objects.get(nazwa='Uderzenie')).save()
Zagrozenia_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea polarised'), zagrozenie=Zagrozenie.objects.get(nazwa='UV/IR')).save()
Zagrozenia_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea mirror'), zagrozenie=Zagrozenie.objects.get(nazwa='Uderzenie')).save()
Zagrozenia_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea mirror'), zagrozenie=Zagrozenie.objects.get(nazwa='UV/IR')).save()
Zagrozenia_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea clear'), zagrozenie=Zagrozenie.objects.get(nazwa='Uderzenie')).save()
Zagrozenia_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea clear'), zagrozenie=Zagrozenie.objects.get(nazwa='UV/IR')).save()

################## Zawody_Dla_Produktu ##################
Zawody_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea polarised'), zawod=Zawod.objects.get(nazwa='Budownictwo i roboty publiczne')).save()
Zawody_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea polarised'), zawod=Zawod.objects.get(nazwa='Prace remontowe/rzemiosło')).save()
Zawody_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea polarised'), zawod=Zawod.objects.get(nazwa='Energia wiatrowa')).save()
Zawody_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea mirror'), zawod=Zawod.objects.get(nazwa='Budownictwo i roboty publiczne')).save()
Zawody_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea mirror'), zawod=Zawod.objects.get(nazwa='Prace remontowe/rzemiosło')).save()
Zawody_Dla_Produktu.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea clear'), zawod=Zawod.objects.get(nazwa='Prace remontowe/rzemiosło')).save()

################## Promowanie ##################
Polecane.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea polarised'), data_zakonczenia=timezone.now()).save()
