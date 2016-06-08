# -*- coding: utf-8 -*-
from produkt.models import *
from django.utils import timezone

################## Firma ##################
Firma.objects.create(nazwa='Kilauea').save()
Firma.objects.create(nazwa='Saba').save()
Firma.objects.create(nazwa='Deltaplus').save()

################## Kolor ##################
Kolor.objects.create(nazwa='Polaryzacyjne').save()
Kolor.objects.create(nazwa='Odblaskowy').save()
Kolor.objects.create(nazwa='Bezbarwny').save()
Kolor.objects.create(nazwa='Czarny').save()
Kolor.objects.create(nazwa='Żółty').save()
Kolor.objects.create(nazwa='Brak').save()

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
Typ_Odziezy.objects.create(nazwa='Ochrona głowy', url='ochrona_głowy').save()

Dziedzina_Odziezy.objects.create(nazwa='Ochrona wzroku', url='ochrona_wzroku', typ=Typ_Odziezy.objects.get(nazwa='Ochrona głowy')).save()
Dziedzina_Odziezy.objects.create(nazwa='Ochrona czaszki', url='ochrona_czaszki', typ=Typ_Odziezy.objects.get(nazwa='Ochrona głowy')).save()
Dziedzina_Odziezy.objects.create(nazwa='Ochrona słuchu', url='ochrona_słuchu', typ=Typ_Odziezy.objects.get(nazwa='Ochrona głowy')).save()
Dziedzina_Odziezy.objects.create(nazwa='Ochrona dróg oddechowych', url='ochrona_dróg_oddechowych', typ=Typ_Odziezy.objects.get(nazwa='Ochrona głowy')).save()

Rodzaj_Odziezy.objects.create(nazwa='Okulary ochronne', url='okulary_ochronne', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona wzroku')).save()
Rodzaj_Odziezy.objects.create(nazwa='Gogle ochronne', url='gogle_ochronne', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona wzroku')).save()
Rodzaj_Odziezy.objects.create(nazwa='Przyłbice spawalnicze', url='przyłbice_spawalnicze', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona wzroku')).save()
Rodzaj_Odziezy.objects.create(nazwa='Osłony ochronne', url='osłony_ochronne', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona wzroku')).save()

Rodzaj_Odziezy.objects.create(nazwa='Hełmy ochronne', url='hełmy_ochronne', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona czaszki')).save()
Rodzaj_Odziezy.objects.create(nazwa='Hełmy lekkie', url='hełmy_lekkie', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona czaszki')).save()

Rodzaj_Odziezy.objects.create(nazwa='Nauszniki przeciwhałasowe', url='nauszniki_przeciwhałasowe', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona słuchu')).save()
Rodzaj_Odziezy.objects.create(nazwa='Wkładki przeciwhałasowe', url='wkładki_przeciwhałasowe', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona słuchu')).save()

Rodzaj_Odziezy.objects.create(nazwa='Maski jednorazowe', url='maski_jednorazowe', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona dróg oddechowych')).save()
Rodzaj_Odziezy.objects.create(nazwa='Maski wielokrotnego użytku', url='maski_wielokrotnego_użytku', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Ochrona dróg oddechowych')).save()

################## Ochrona rąk: Kontenery ##################
Typ_Odziezy.objects.create(nazwa='Ochrona rąk', url='ochrona_rąk').save()

Dziedzina_Odziezy.objects.create(nazwa='Rękawice high-tech', url='rękawice_hightech', typ=Typ_Odziezy.objects.get(nazwa='Ochrona rąk')).save()
Dziedzina_Odziezy.objects.create(nazwa='Rękawice syntetyczne', url='rękawice_syntetyczne', typ=Typ_Odziezy.objects.get(nazwa='Ochrona rąk')).save()
Dziedzina_Odziezy.objects.create(nazwa='Rękawice skórzane', url='rękawice_skórzane', typ=Typ_Odziezy.objects.get(nazwa='Ochrona rąk')).save()
Dziedzina_Odziezy.objects.create(nazwa='Rękawice tekstylne', url='rękawice_tekstylne', typ=Typ_Odziezy.objects.get(nazwa='Ochrona rąk')).save()

Rodzaj_Odziezy.objects.create(nazwa='Do prac z ostrymi przedmiotami', url='Do_prac_z_ostrymi_przedmiotami', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Rękawice high-tech')).save()
Rodzaj_Odziezy.objects.create(nazwa='Do prac antyelektrostatycznych', url='Do_prac_antyelektrostatycznych', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Rękawice high-tech')).save()
Rodzaj_Odziezy.objects.create(nazwa='Do prac precyzyjnych', url='Do_prac_precyzyjnych', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Rękawice high-tech')).save()

Rodzaj_Odziezy.objects.create(nazwa='Do prac ciężkich', url='Do_prac_ciężkich', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Rękawice syntetyczne')).save()

################## Ochrona nóg: Kontenery ##################
Typ_Odziezy.objects.create(nazwa='Ochrona nóg', url='ochrona_nóg').save()

Dziedzina_Odziezy.objects.create(nazwa='Obuwie', url='obuwie', typ=Typ_Odziezy.objects.get(nazwa='Ochrona nóg')).save()
Dziedzina_Odziezy.objects.create(nazwa='Obuwie wysokie', url='obuwie_wysokie', typ=Typ_Odziezy.objects.get(nazwa='Ochrona nóg')).save()
Dziedzina_Odziezy.objects.create(nazwa='Akcesoria', url='akcesoria', typ=Typ_Odziezy.objects.get(nazwa='Ochrona nóg')).save()

Rodzaj_Odziezy.objects.create(nazwa='Trek work', url='trek_work', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Obuwie')).save()
Rodzaj_Odziezy.objects.create(nazwa='Waterproof', url='waterproof', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Obuwie')).save()
Rodzaj_Odziezy.objects.create(nazwa='X-Run', url='x-run', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Obuwie')).save()

################## Ochrona nóg: Kontenery ##################
Typ_Odziezy.objects.create(nazwa='Ochrona przed upadkiem z wysokości', url='ochrona_przed_upadkiem_z_wysokości').save()

Dziedzina_Odziezy.objects.create(nazwa='Szelki bezpieczeństwa', url='szelki_bezpieczeństwa', typ=Typ_Odziezy.objects.get(nazwa='Ochrona przed upadkiem z wysokości')).save()
Dziedzina_Odziezy.objects.create(nazwa='Elementy kotwiczące', url='elementy_kotwiczące', typ=Typ_Odziezy.objects.get(nazwa='Ochrona przed upadkiem z wysokości')).save()

Rodzaj_Odziezy.objects.create(nazwa='Szelki chroniące przed upadkiem', url='Szelki_chroniące_przed_upadkiem', dziedzina=Dziedzina_Odziezy.objects.get(nazwa='Szelki bezpieczeństwa')).save()

################## Produkty ##################
Produkt.objects.create(nazwa='Kilauea polarised',
                       opis='Okulary z poliwęglanu. Sportowy wygląd. Nylonowa matowa oprawka dla większej wygody i trwałości.',
                       firma=Firma.objects.get(nazwa='Kilauea'),
                       kolor=Kolor.objects.get(nazwa='Polaryzacyjne'),
                       waga=28,
                       sztuk=100,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Okulary ochronne')
                       ).save()

Produkt.objects.create(nazwa='Kilauea mirror',
                       opis='Okulary z poliwęglanu. Sportowy wygląd. Nylonowa matowa oprawka dla większej wygody i trwałości.',
                       firma=Firma.objects.get(nazwa='Kilauea'),
                       kolor=Kolor.objects.get(nazwa='Odblaskowy'),
                       waga=28,
                       sztuk=100,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Okulary ochronne')
                       ).save()

Produkt.objects.create(nazwa='Kilauea clear',
                       opis='Okulary z poliwęglanu. Sportowy wygląd. Nylonowa matowa oprawka dla większej wygody i trwałości.',
                       firma=Firma.objects.get(nazwa='Kilauea'),
                       kolor=Kolor.objects.get(nazwa='Bezbarwny'),
                       waga=28,
                       sztuk=100,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Okulary ochronne')
                       ).save()

Produkt.objects.create(nazwa='Saba',
                       opis='Gogle z poliwęglanu, bezbarwne. Wentylacja pośrednia. Taśma nagłowia nie zawierająca gumy (bez lateksu). Miękka oprawka z PVC. Innowacyjny system regulacji ROTOR (opatentowany), łatwy w użytkowaniu i wygodny w noszeniu.',
                       firma=Firma.objects.get(nazwa='Saba'),
                       kolor=Kolor.objects.get(nazwa='Bezbarwny'),
                       waga=122,
                       sztuk=60,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Gogle ochronne')
                       ).save()

Produkt.objects.create(nazwa='Venicut53',
                       opis='Rękawica z włukna polietylenowego wyskoiej odporności Deltanocut. Powłoka z pianki nitrylowej na stronie chwytnej i końcach palców. Nadgarstek elastyczny 10 cm. Ścieg 13.',
                       firma=Firma.objects.get(nazwa='Deltaplus'),
                       kolor=Kolor.objects.get(nazwa='Czarny'),
                       waga=0,
                       sztuk=60,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Do prac z ostrymi przedmiotami')
                       ).save()

Produkt.objects.create(nazwa='Venicut32',
                       opis='Relawoca z włókna wysokiej odporności DELTAnocut. Powłoka poliuretanowa na stronie chwytnej i końcach palców. Ścieg 15.',
                       firma=Firma.objects.get(nazwa='Deltaplus'),
                       kolor=Kolor.objects.get(nazwa='Żółty'),
                       waga=0,
                       sztuk=60,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Do prac z ostrymi przedmiotami')
                       ).save()

Produkt.objects.create(nazwa='TW400 S3 SRC',
                       opis='Cholewka: pełna skóra licowa, wodoodporna S3, ze wzmocnieniem noska z kauczuku. Podszewka: poliamid Cambrelle pochłaniający wilgoć. Wkładka: wymienna, wstępnie uformowana, poliester na piance PU. Podszewka: zgrzewana, wkładka z PU z pochłaniaczem energii Panoshock. Warstwa ścierna: kauczuk nitryl. Obuwie amagnetyczne.',
                       firma=Firma.objects.get(nazwa='Deltaplus'),
                       kolor=Kolor.objects.get(nazwa='Czarny'),
                       waga=710,
                       sztuk=5,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Trek work')
                       ).save()

Produkt.objects.create(nazwa='TW300 S3 SRC',
                       opis='Cholewka: pełna skóra licowa, wodoodporna S3, ze wzmocnieniem noska z kauczuku. Podszewka: poliamid Cambrelle pochłaniający wilgoć. Wkładka: wymienna, wstępnie uformowana, poliester na piance PU. Podszewka: zgrzewana, wkładka z PU z pochłaniaczem energii Panoshock. Warstwa ścierna: kauczuk nitryl. Obuwie amagnetyczne.',
                       firma=Firma.objects.get(nazwa='Deltaplus'),
                       kolor=Kolor.objects.get(nazwa='Czarny'),
                       waga=680,
                       sztuk=5,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Trek work')
                       ).save()

Produkt.objects.create(nazwa='Eolien har35',
                       opis='Szelki dwukolorowe z pasem podtrzymującym. 3 punkty zaczepowe do asekuracji (tylny, przedni prawy, przedni lewy). 4 klamry regulacyjne. Pas podtrzymujący z oparciem formowanym na gorąco zamykany na szeroki rzep dla większego komfortu. Możliwość obrotu 120 st. 2 punkty zaczepowe boczne. 1 automatyczna klamra regulacyjna. Oparcie wyścielane gąbką.',
                       firma=Firma.objects.get(nazwa='Deltaplus'),
                       kolor=Kolor.objects.get(nazwa='Brak'),
                       waga=2000,
                       sztuk=5,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Szelki chroniące przed upadkiem')
                       ).save()

Produkt.objects.create(nazwa='Anatom har32',
                       opis='Szelki dwukolorowe. 2 punkty zaczepowe do asekuracji( tylny i przedni).  4 klamry regulacyjne.',
                       firma=Firma.objects.get(nazwa='Deltaplus'),
                       kolor=Kolor.objects.get(nazwa='Brak'),
                       waga=680,
                       sztuk=1400,
                       rodzaj=Rodzaj_Odziezy.objects.get(nazwa='Szelki chroniące przed upadkiem')
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
Polecane.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea mirror'), data_zakonczenia=timezone.now()).save()
Polecane.objects.create(produkt=Produkt.objects.get(nazwa='Kilauea clear'), data_zakonczenia=timezone.now()).save()
