# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from dodatek.views import *
import pickle, time, os, operator


def Wyswietl_Komunikat_O_Wyjatku(e, nazwa_wyjatku, numer_wyjatku=None,
                                 nazwa_produktu=None, url=None):
    komunikat = ''
    if numer_wyjatku:
        komunikat += '\n\n' + str(numer_wyjatku)

    komunikat += '\n\t WYJĄTEK: %s: \n' % nazwa_wyjatku
    komunikat += '\t\t %s \n' % str(e)

    if nazwa_produktu:
        komunikat += '\t\t produkt.nazwa: %s \n' % nazwa_produktu

    if url:
        komunikat += '\t\tadres strony: %s \n' % url

    print(komunikat)
    os.system('echo "%s" >> sql/protekt.log' % komunikat)

def Usun_Biale_Znaki(tekst):

    if tekst:

        tekst = tekst.translate(str.maketrans('', '', '\t\n\r'))

        # usuwanie spacji przed tekstem
        while tekst[0] == ' ':
            tekst = tekst[1:len(tekst)]

        # usuwanie spacji za tekstem
        while tekst[len(tekst)-1] == ' ':
            tekst = tekst[0:len(tekst)-2]

    return tekst


class Konwerter:
    html = ''
    produkt = {}

    def Pobierz_Nazwa(self):
        numer = self.html.find('id="produkt_head"')
        nazwa = self.html[numer:]

        numer = nazwa.find('<strong>')
        nazwa = nazwa[numer:]

        numer = nazwa.find('<span ')
        nazwa = nazwa[numer:]

        poczatek = nazwa.find('>') + 1
        koniec = nazwa.find('</span>')

        self.produkt['nazwa'] = \
            Usun_Biale_Znaki(nazwa[poczatek:koniec])

    def Pobierz_Opis(self):

        numer = self.html.find('id="produkt_opis"')
        opis = self.html[numer:]

        opis = Kierownik.Wytnij_Blok_HTML(opis, '<p>', '</p>')
        opis = opis.replace('<span style="font-size: small;">', '')
        opis = opis.replace('</span>', '')

        self.produkt['opis'] = \
            Usun_Biale_Znaki(opis)

    def Pobierz_Slowa_Kluczowe(self):
        self.produkt['slowa_kluczowe'] = [
            self.produkt['nazwa'],
            self.produkt['nazwa'],
            self.produkt['nazwa'],
            Usun_Polskie_Znaki(self.produkt['nazwa']),
            Usun_Polskie_Znaki(self.produkt['opis']),
            Usun_Polskie_Znaki(self.produkt['producent']),
            Usun_Polskie_Znaki(self.produkt['rodzaj']),
        ]

    def Pobierz_Rozmiar(self):
        pass

    def Pobierz_Producent(self):
        self.produkt['producent'] = 'Protekt'

    def Pobierz_Kolor(self):
        self.produkt['kolor'] = 'Brak'

    def Pobierz_Rodzaj(self, rodzaj):
        self.produkt['rodzaj'] = rodzaj

    def Pobierz_Certyfikaty(self):
        pass

    def Pobierz_Zagrozenia(self):
        pass

    def Pobierz_Zawody(self):
        pass

    def Pobierz_Zdjecie(self):
        numer = self.html.find('id="produkt_mid_pic"')
        zdjecie = self.html[numer:]

        numer = zdjecie.find('<img ')
        zdjecie = zdjecie[numer:]

        numer = zdjecie.find('src="')
        zdjecie = zdjecie[numer:]

        poczatek = 5
        koniec = zdjecie.find('.jpg') + 4

        self.produkt['zdjecie'] = \
            zdjecie[poczatek:koniec]

    @staticmethod
    def Wytnij_Blok_Strony_Produktu(html):

        numer = html.find('id="produkt"')
        html = html[numer - 10:]

        return Kierownik.Wytnij_Blok_HTML(html, '<div', '</div>')

    def __init__(self, html='', rodzaj='', produkt=None):

        if produkt: # dla gotowego produktu
            self.produkt = produkt
            return

        self.html = self.Wytnij_Blok_Strony_Produktu(html)
        self.produkt = {
            'nazwa': '',
            'opis': '',
            'slowa_kluczowe': '',
            'rozmiar': '',
            'producent': '',
            'kolor': '',
            'rodzaj': '',
            'certyfikaty': [],
            'zagrozenia': [],
            'zawody': [],
            'zdjecie': '',
        }

        # uzupełnianie słownika
        self.Pobierz_Nazwa()
        self.Pobierz_Opis()
        self.Pobierz_Rozmiar()
        self.Pobierz_Producent()
        self.Pobierz_Kolor()
        self.Pobierz_Rodzaj(rodzaj)
        self.Pobierz_Certyfikaty()
        self.Pobierz_Zagrozenia()
        self.Pobierz_Zawody()
        self.Pobierz_Zdjecie()

        self.Pobierz_Slowa_Kluczowe()


class Baza_Danych:
    produkt = {}
    produkt_zapisany = None

    def Sprawdz_Podklasy(self, typ, dziedzina):

        # one to many
        if not Producent.objects.filter(nazwa=self.produkt['producent']):
            Producent.objects.create(nazwa=self.produkt['producent']).save()

        if not Kolor.objects.filter(nazwa=self.produkt['kolor']):
            Kolor.objects.create(nazwa=self.produkt['kolor']).save()

            # kontenery
        if not Typ_Odziezy.objects.filter(nazwa=typ):
            Typ_Odziezy.objects.create(nazwa=typ,
                                       url=Konwertuj_Nazwe_Na_URL(typ)).save()

        if not Dziedzina_Odziezy.objects.filter(nazwa=dziedzina, typ=Typ_Odziezy.objects.get(nazwa=typ)):
            Dziedzina_Odziezy.objects.create(nazwa=dziedzina,
                                             url=Konwertuj_Nazwe_Na_URL(dziedzina),
                                             typ=Typ_Odziezy.objects.get(nazwa=typ)).save()

        if not Rodzaj_Odziezy.objects.filter(nazwa=self.produkt['rodzaj'],
                                             dziedzina=Dziedzina_Odziezy.objects.get(nazwa=dziedzina,
                                                                                     typ=Typ_Odziezy.objects.get(
                                                                                         nazwa=typ))):
            Rodzaj_Odziezy.objects.create(nazwa=self.produkt['rodzaj'],
                                          url=Konwertuj_Nazwe_Na_URL(self.produkt['rodzaj']),
                                          dziedzina=Dziedzina_Odziezy.objects.get(nazwa=dziedzina,
                                                                                  typ=Typ_Odziezy.objects.get(
                                                                                      nazwa=typ))).save()

            # many to many
        for certyfikat in self.produkt['certyfikaty']:
            if not Certyfikat.objects.filter(numer=certyfikat[0]):
                Certyfikat.objects.create(numer=certyfikat[0],
                                          szczegoly=certyfikat[1]).save()

    def Konwertuj_MTM(self):  # ManyToMany

        certyfikaty = self.produkt['certyfikaty']
        self.produkt['certyfikaty'] = \
            [Certyfikat.objects.get(numer=c[0]) for c in certyfikaty]

        try:

            zagrozenia = self.produkt['zagrozenia']
            self.produkt['zagrozenia'] = \
                [Zagrozenie.objects.get(nazwa=z) for z in zagrozenia]

        except Exception as e:
            self.produkt['zagrozenia'] = []
            Wyswietl_Komunikat_O_Wyjatku(e, 'Baza_Danych.Konwertuj_MTM()',
                                         nazwa_produktu=self.produkt['nazwa'])

        try:

            zawody = self.produkt['zawody']
            self.produkt['zawody'] = \
                [Zawod.objects.get(nazwa=z) for z in zawody]

        except Exception as e:
            self.produkt['zawody'] = []
            Wyswietl_Komunikat_O_Wyjatku(e, 'Baza_Danych.Konwertuj_MTM()',
                                         nazwa_produktu=self.produkt['nazwa'])

    def Dodaj_Produkt(self, typ, dziedzina):

        self.produkt_zapisany = Produkt.objects.create(
            nazwa=self.produkt['nazwa'],
            opis=self.produkt['opis'],
            slowa_kluczowe=self.produkt['slowa_kluczowe'],
            rozmiar=self.produkt['rozmiar'],
            producent=Producent.objects.get(nazwa=self.produkt['producent']),
            kolor=Kolor.objects.get(nazwa=self.produkt['kolor']),
            rodzaj=Rodzaj_Odziezy.objects.get(nazwa=self.produkt['rodzaj'],
                                              dziedzina=Dziedzina_Odziezy.objects.get(
                                                  nazwa=dziedzina,
                                                  typ=Typ_Odziezy.objects.get(nazwa=typ))
                                              )
        )

        self.produkt_zapisany.save()

        # certyfikaty, zagrożenia, zawody
        for c in self.produkt['certyfikaty']:
            self.produkt_zapisany.certyfikaty.add(c)

        for z in self.produkt['zagrozenia']:
            self.produkt_zapisany.zagrozenia.add(z)

        for z in self.produkt['zawody']:
            self.produkt_zapisany.zawody.add(z)

            # zdjęcie - jeżeli nie ma kopi produktów
        if not Kierownik.odczyt_produktow:
            self.produkt_zapisany.Zapisz_Zdjecie_URL(self.produkt['zdjecie'])

        else:
            nazwa = '/static/img/produkt/{0}.jpeg'.format(self.produkt_zapisany.pk)
            self.produkt_zapisany.zdjecie.name = nazwa
            self.produkt_zapisany.save()

    def Dodaj_Meta_Tagi(self):

        Meta_Tagi.objects.create(
            adres_strony='/produkt/%s/' % str(self.produkt_zapisany.pk),
            description=self.produkt_zapisany.opis[0:154],
            og_type='produkt',
            og_url='http://asbhp.arbuz.team/produkt/%s/' % str(self.produkt_zapisany.pk),
            og_image=str(self.produkt_zapisany.zdjecie)
        ).save()

    def __init__(self, produkt, typ, dziedzina):
        self.produkt = produkt

        self.Sprawdz_Podklasy(typ, dziedzina)
        self.Konwertuj_MTM()

        try:

            self.Dodaj_Produkt(typ, dziedzina)

        except Exception as e:
            Kierownik.numer_wyjatku += 1
            Wyswietl_Komunikat_O_Wyjatku(e, 'Baza_Danych.Dodaj_Produkt()',
                                         Kierownik.numer_wyjatku, self.produkt['nazwa'])


class Kierownik:
    adresy_url = {} # {typ: {dziedzina: {rodzaj: url}}, ...}
    zrodlo_strony = ''
    firefox = None
    numer_wyjatku = 0
    odczyt_produktow = False

    @staticmethod
    def WAURL_Pobierz_Nazwe(html):

        nazwa = Kierownik.Wytnij_Blok_HTML(html, '<a ', '</a>')

        poczatek = nazwa.find('>') + 1
        nazwa = nazwa[poczatek:]

        # nazwa przycisku
        return Usun_Biale_Znaki(nazwa)

    @staticmethod
    def WAURL_Pobierz_URL(html):

        nazwa = Kierownik.Wytnij_Blok_HTML(html, '<a ', '</a>')

        poczatek = nazwa.find('href="') + 6
        nazwa = nazwa[poczatek:]

        # adres url
        koniec = nazwa.find('"')
        return 'http://protekt.com.pl/' + \
               nazwa[0:koniec].replace('&amp;', '&')

    def WAURL_Pobierz_Liste_URL(self, url):

        self.Pobieranie_Zrodla_Strony(url)
        adresy = []

        # sprawdzam ilość zakładek do sprawdzenia
        numer = self.zrodlo_strony.find('images/lista_prod_03_a.png')
        html = self.zrodlo_strony[numer:]

        html = self.Wytnij_Blok_HTML(html, '<div', '</div>')

        numer = html.rfind('<a ')
        html = html[numer:]
        liczba_zakladek = int(html[html.find('>') + 1])

        # pobieram adresy produktów z kolenych zakładek
        for numer_zakladki in range(1, liczba_zakladek + 1):

            # pobieranie kolejnych zakładek
            self.Pobieranie_Zrodla_Strony(url + '&cp={0}'.format(numer_zakladki))

            numer = self.zrodlo_strony.find('id="kategorie_lista"')
            html = self.zrodlo_strony[numer:]

            html = self.Wytnij_Blok_HTML(html, '<table', '</table>')

            while '<tr>' in html:

                numer = html.find('<a ')
                html = html[numer:]

                numer = html.find('href="') + 6
                html = html[numer:]

                koniec = html.find('"')
                if html[:koniec]:
                    if 'Kamizelki' in html[:koniec]:
                        print(url + '&cp={0}'.format(numer_zakladki))

                    adresy.append('http://protekt.com.pl/' +
                                  html[:koniec].replace('&amp;', '&'))

        return adresy

    def Wczytaj_Adresy_URL(self):

        # wczytuje wcześniej wczytane adresy
        if os.path.exists('sql/protekt.urls'):
            with open('sql/protekt.urls', 'rb') as plik:
                self.adresy_url = pickle.load(plik)

            return

        self.Pobieranie_Zrodla_Strony(
            'http://protekt.com.pl/?page=kategoria')

        # wycięcie odpowiedniego bloku
        numer = self.zrodlo_strony.find('name="kat_form"')
        html = self.Wytnij_Blok_HTML(self.zrodlo_strony[numer:], '<table', '</table>')

        # pobieram typ
        while '<tr>' in html:

            # wycinam blok typ
            html_typ = self.Wytnij_Blok_HTML(html, '<tr>', '</tr>')
            html = html.replace('<tr>' + html_typ + '</tr>', ' ')

            typ = self.WAURL_Pobierz_Nazwe(html_typ)
            self.adresy_url[typ] = {}

            # pobieram kolejny blok i sprawdzam, czy to dziedzina
            podkategoria_typ = self.Wytnij_Blok_HTML(html, '<tr>', '</tr>')
            if '<table' in str(podkategoria_typ):

                html = html.replace('<tr>' + podkategoria_typ + '</tr>', ' ')
                podkategoria_typ = self.Wytnij_Blok_HTML(podkategoria_typ, '<table', '</table>')

                # pobieram dziedzina
                while '<tr>' in str(podkategoria_typ): # str() dla przypadku None

                    # wycinam blok dziedzina
                    html_dziedzina = self.Wytnij_Blok_HTML(podkategoria_typ, '<tr>', '</tr>')
                    podkategoria_typ = podkategoria_typ.replace('<tr>' + html_dziedzina + '</tr>', ' ')

                    dziedzina = self.WAURL_Pobierz_Nazwe(html_dziedzina)
                    self.adresy_url[typ][dziedzina] = {}

                    # pobieram kolejny blok i sprawdzam, czy to rodzaj
                    podkategoria_dziedzina = self.Wytnij_Blok_HTML(podkategoria_typ, '<tr>', '</tr>')
                    if '<table' in str(podkategoria_dziedzina): # str() dla przypadku None

                        podkategoria_typ = podkategoria_typ.replace('<tr>' + podkategoria_dziedzina + '</tr>', ' ')
                        podkategoria_dziedzina = self.Wytnij_Blok_HTML(podkategoria_dziedzina, '<table', '</table>')

                        # pobieram dziedzina
                        while '<tr>' in str(podkategoria_dziedzina):  # str() dla przypadku None

                            # wycinam blok dziedzina
                            html_rodzaj = self.Wytnij_Blok_HTML(podkategoria_dziedzina, '<tr>', '</tr>')
                            podkategoria_dziedzina = podkategoria_dziedzina.replace('<tr>' + html_rodzaj + '</tr>', ' ')

                            rodzaj = self.WAURL_Pobierz_Nazwe(html_rodzaj)
                            adres = self.WAURL_Pobierz_URL(html_rodzaj)
                            self.adresy_url[typ][dziedzina][rodzaj] = self.WAURL_Pobierz_Liste_URL(adres)

                            # pobieram kolejny blok i sprawdzam, czy to dalej niż rodzaj
                            podkategoria_rodzaj = self.Wytnij_Blok_HTML(podkategoria_dziedzina, '<tr>', '</tr>')
                            if '<table' in str(podkategoria_rodzaj):
                                podkategoria_dziedzina = podkategoria_dziedzina.replace('<tr>' + podkategoria_rodzaj + '</tr>', ' ')

                    else:

                        adres = self.WAURL_Pobierz_URL(html_dziedzina)
                        self.adresy_url[typ][dziedzina] = self.WAURL_Pobierz_Liste_URL(adres)

            else:

                adres = self.WAURL_Pobierz_URL(html_typ)
                self.adresy_url[typ] = self.WAURL_Pobierz_Liste_URL(adres)


    def Zapisz_Adresy_URL(self):
        if not os.path.exists('sql/protekt.urls'):
            with open('sql/protekt.urls', 'wb') as plik:
                pickle.dump(self.adresy_url, plik, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def Wytnij_Blok_HTML(html, znacznik_otwierajacy, znacznik_zamykajacy):
        # Wycina pierwszy napotkany blok między podanymi znacznikami

        poczatek = html.find(znacznik_otwierajacy)
        blok = html[poczatek:]

        # sprawdzam html po znakach
        len_zo = len(znacznik_otwierajacy)
        len_zz = len(znacznik_zamykajacy)
        poziom_znacznika = 1
        blok = blok[len_zo:]

        for numer, znak in enumerate(blok):

            # znalazł znacznik otwierający
            if znak == znacznik_otwierajacy[0]:
                if znacznik_otwierajacy in blok[numer:numer + len_zo]:
                    poziom_znacznika += 1

                    # znalazł znacznik zamykający
            if znak == znacznik_zamykajacy[0]:
                if znacznik_zamykajacy in blok[numer:numer + len_zz]:
                    poziom_znacznika -= 1

                    # zamknął ostatni znacznik
            if poziom_znacznika == 0:
                return blok[0:numer]

    def Pobieranie_Zrodla_Strony(self, url, nacisnij_link=None):

        # pobieranie źródła
        self.firefox.get(url)
        # time.sleep(2) # oczekuje załadowania strony

        # naciśnięcie na link (event)
        if nacisnij_link:
            link = self.firefox.find_element_by_link_text(nacisnij_link)
            link.click()
            #time.sleep(4)

            # zamknięcie przeglądarki
        self.zrodlo_strony = self.firefox.page_source

    def Dodaj_Produkt_Do_Bazy_Danych(self, url, typ, dziedzina,
                                     rodzaj, pickler):

        if Kierownik.odczyt_produktow:  # odczytuję produkty z istniejącego pliku
            produkt = pickler.load()

            # zapisywanie
            Baza_Danych(produkt, typ, dziedzina)

        else:

            try:

                self.Pobieranie_Zrodla_Strony(url)
                konwerter = Konwerter(self.zrodlo_strony, rodzaj)

                # zapisywanie
                pickler.dump(konwerter.produkt)
                Baza_Danych(konwerter.produkt, typ, dziedzina)

            except Exception as e:
                Kierownik.numer_wyjatku += 1
                Wyswietl_Komunikat_O_Wyjatku(e, 'Kierownik.Dodaj_Produkt_Do_Bazy_Danych()',
                                             Kierownik.numer_wyjatku, url=url)


    def __init__(self):

        # ustawienia przeglądarki
        binary = FirefoxBinary('/home/endo93/Firefox 46.0/firefox')
        self.firefox = webdriver.Firefox(firefox_binary=binary)
        os.system('rm sql/protekt.log')

        self.Wczytaj_Adresy_URL()
        self.Zapisz_Adresy_URL()

        # pickler - zapis/odczyt produktów z pliku
        pickler = None
        plik = None

        if os.path.exists('sql/protekt.prod'):
            Kierownik.odczyt_produktow = True
            plik = open('sql/protekt.prod', 'rb')
            pickler = pickle.Unpickler(plik)

        else: # do zapisywania
            plik = open('sql/protekt.prod', 'wb')
            pickler = pickle.Pickler(plik, pickle.HIGHEST_PROTOCOL)

        # dla każdego adresu url
        for typ in self.adresy_url:

            if isinstance(self.adresy_url[typ], dict):
                for dziedzina in self.adresy_url[typ]:

                    if isinstance(self.adresy_url[typ][dziedzina], dict):
                        for rodzaj in self.adresy_url[typ][dziedzina]:

                            if isinstance(self.adresy_url[typ][dziedzina][rodzaj], dict):
                                print('Ups...')

                            else:
                                for url in self.adresy_url[typ][dziedzina][rodzaj]:
                                    self.Dodaj_Produkt_Do_Bazy_Danych(url, typ, dziedzina,
                                                                      rodzaj, pickler)

                    else:
                        for url in self.adresy_url[typ][dziedzina]:
                            self.Dodaj_Produkt_Do_Bazy_Danych(url, typ, dziedzina,
                                                              'Inne', pickler)

            else:
                for url in self.adresy_url[typ]:
                    self.Dodaj_Produkt_Do_Bazy_Danych(url, typ, 'Inne',
                                                      'Inne', pickler)

        plik.close()
        self.firefox.close()


Kierownik()
