# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from dodatek.views import *
import pickle
import time
import os



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
    os.system('echo "%s" >> sql/deltaplus.log' % komunikat)




class Konwerter:

    html = ''
    produkt = {}


    def Pobierz_Nazwa(self):

        numer = self.html.find('<div id="descArticle"')
        nazwa = self.html[numer:-1]

        poczatek = nazwa.find('<h1>') + 4
        koniec = nazwa.find('</h1>')

        self.produkt['nazwa'] = \
            nazwa[poczatek:koniec]


    def Pobierz_Opis(self):

        numer = self.html.find('<section id="sectionCarac"')
        opis = self.html[numer:-1]

        numer = opis.find('<section class="blocContenu blocContenu-first"')
        opis = opis[numer:-1]

        poczatek = opis.find('<div>') + 5
        koniec = opis.find('</div>')

        self.produkt['opis'] = \
            opis[poczatek:koniec]


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

        numer = self.html.find('<section class="groupingRules"')
        rozmiar = self.html[numer:-1]

        numer = rozmiar.find('rozmiar')
        rozmiar = rozmiar[numer:-1]

        poczatek = rozmiar.find('<p>') + 3
        koniec = rozmiar.find('</p>')

        self.produkt['rozmiar'] = \
            rozmiar[poczatek:koniec].translate(str.maketrans('', '', '\t\n'))


    def Pobierz_Producent(self):
        self.produkt['producent'] = 'DeltaPlus'


    def Pobierz_Kolor(self):

        numer = self.html.find('<section class="groupingRules"')
        kolor = self.html[numer:-1]

        numer = kolor.find('KOLOR')
        kolor = kolor[numer:-1]

        numer = kolor.find('</div>')
        kolor = kolor[0:numer]

        poczatek = kolor.find('<p>') + 3
        koniec = kolor.find('</p>')

        self.produkt['kolor'] = \
            kolor[poczatek:koniec].translate(str.maketrans('', '', '\t\n\xe2\x80\x8b'))


    def Pobierz_Rodzaj(self, rodzaj):
        self.produkt['rodzaj'] = rodzaj


    def Pobierz_Certyfikaty(self):

        numer = self.html.find('<section id="sectionNormes"')
        certyfikaty = self.html[numer:-1]

            # dopóki znajduje kolejne bloki
        while '<div class="row-fluid norme">' in certyfikaty:

                # znajduję blok
            numer = certyfikaty.find('<div class="row-fluid norme">')
            certyfikaty = certyfikaty[numer:-1]

            numer = certyfikaty.find('class="normLib">')
            certyfikaty = certyfikaty[numer:-1]

            poczatek = certyfikaty.find('>') + 1
            koniec = certyfikaty.find('<i')

                # zapisuję
            self.produkt['certyfikaty'].append(
                certyfikaty[poczatek:koniec].
                    translate(str.maketrans('', '', '\t\n')).split('\xa0')[0:2])


    def Pobierz_Zagrozenia(self):

            # wyciągam pole między tymi znacznikami
        numer = self.html.find('<div class="linePictos blocContenu">')
        zagrozenia = self.html[numer+1:-1] # "+1" aby nie szukać tego samego

            # drugi blok o takiej samej klasie
        numer = zagrozenia.find('<div class="linePictos blocContenu">')
        zagrozenia = zagrozenia[numer:-1]

        koniec = zagrozenia.find('<!--')
        zagrozenia = zagrozenia[0:koniec]

            # dopóki znajduje kolejne bloki
        while '<div class="blocProductUse">' in zagrozenia:

                # znajduję blok
            numer = zagrozenia.find('<div class="blocProductUse">')
            zagrozenia = zagrozenia[numer:-1]

                # znajduję tekst
            numer = zagrozenia.find('<span>')
            zagrozenia = zagrozenia[numer+1:-1] # "+1" aby nie szukać tego samego

                # drugi span
            numer = zagrozenia.find('<span>')
            zagrozenia = zagrozenia[numer:-1]

            poczatek = zagrozenia.find('>') + 1
            koniec = zagrozenia.find('</span>')

                # zapisuję
            self.produkt['zagrozenia'].append(
                zagrozenia[poczatek:koniec])


    def Pobierz_Zawody(self):

            # wyciągam pole między tymi znacznikami
        numer = self.html.find('<div class="linePictos blocContenu">')
        zawody = self.html[numer:-1]

        koniec = zawody.find('<!--')
        zawody = zawody[0:koniec]

            # dopóki znajduje kolejne bloki
        while '<div class="blocProductUse">' in zawody:

                # znajduję blok
            numer = zawody.find('<div class="blocProductUse">')
            zawody = zawody[numer:-1]

                # znajduję tekst
            numer = zawody.find('<span id="picto_')
            zawody = zawody[numer:-1]

            poczatek = zawody.find('>') + 1
            koniec = zawody.find('</span>')

                # zapisuję
            self.produkt['zawody'].append(
                zawody[poczatek:koniec])


    def Pobierz_Zdjecie(self):

        numer = self.html.find('<div class="zoomWindow"')
        zdjecie = self.html[numer:-1]

        numer = zdjecie.find('background-image: url')
        zdjecie = zdjecie[numer:-1]

        poczatek = zdjecie.find('/')
        koniec = zdjecie.find('.jpg') + 4

        self.produkt['zdjecie'] = 'https://www.deltaplus.eu' + \
                                  zdjecie[poczatek:koniec]


    def __init__(self, html='', rodzaj='', produkt=None):

        if produkt:
            self.produkt = produkt
            return

        self.html = html
        self.produkt = {
            'nazwa':            '',
            'opis':             '',
            'slowa_kluczowe':   '',
            'rozmiar':          '',
            'producent':        '',
            'kolor':            '',
            'rodzaj':           '',
            'certyfikaty':      [],
            'zagrozenia':       [],
            'zawody':           [],
            'zdjecie':          '',
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

        if not Dziedzina_Odziezy.objects.filter(nazwa=dziedzina):
            Dziedzina_Odziezy.objects.create(nazwa=dziedzina,
                                             url=Konwertuj_Nazwe_Na_URL(dziedzina),
                                             typ=Typ_Odziezy.objects.get(nazwa=typ)).save()

        if not Rodzaj_Odziezy.objects.filter(nazwa=self.produkt['rodzaj']):
            Rodzaj_Odziezy.objects.create(nazwa=self.produkt['rodzaj'],
                                          url=Konwertuj_Nazwe_Na_URL(self.produkt['rodzaj']),
                                          dziedzina=Dziedzina_Odziezy.objects.get(nazwa=dziedzina)).save()

            # many to many
        for certyfikat in self.produkt['certyfikaty']:
            if not Certyfikat.objects.filter(numer=certyfikat[0]):
                Certyfikat.objects.create(numer=certyfikat[0],
                                          szczegoly=certyfikat[1]).save()


    def Konwertuj_MTM(self): # ManyToMany

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


    def Dodaj_Produkt(self):

        self.produkt_zapisany = Produkt.objects.create(
            nazwa=self.produkt['nazwa'],
            opis=self.produkt['opis'],
            slowa_kluczowe=self.produkt['slowa_kluczowe'],
            rozmiar=self.produkt['rozmiar'],
            producent=Producent.objects.get(nazwa=self.produkt['producent']),
            kolor=Kolor.objects.get(nazwa=self.produkt['kolor']),
            rodzaj=Rodzaj_Odziezy.objects.get(nazwa=self.produkt['rodzaj'])
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

            self.Dodaj_Produkt()

        except Exception as e:
            Kierownik.numer_wyjatku += 1
            Wyswietl_Komunikat_O_Wyjatku(e, 'Baza_Danych.Dodaj_Produkt()',
                                         Kierownik.numer_wyjatku, self.produkt['nazwa'])




class Kierownik:

    adresy_url = {} # {typ: {dziedzina: {rodzaj: adres_url}}, ...}
    zrodlo_strony = ''
    firefox = None
    numer_wyjatku = 0
    odczyt_produktow = False

    @staticmethod
    def WAURL_Pobierz_Nazwe(html, tag):

        numer = html.find(tag)
        html = html[numer + 1:-1]  # "+1" uniknie powtórzeń

        poczatek = html.find('<span>') + 6
        koniec = html.find('</span>')

        return html, html[poczatek:koniec] # html się kurczy


    @staticmethod
    def WAURL_Pobierz_URL_Rodzaj(html):

        numer = html.find('<li class="itemLvl4')
        html = html[numer:-1]

        numer = html.find('href="') + 6
        html = html[numer:-1]

        koniec = html.find('"')
        return html[0:koniec]


    def WAURL_Pobierz_URL_Produktow(self, url):

        try:

                # wczytanie źródła strony z naciśniętym linkiem '48'
            self.Pobieranie_Zrodla_Strony(url, '48')

        except NoSuchElementException as e:
            Kierownik.numer_wyjatku += 1
            Wyswietl_Komunikat_O_Wyjatku(e, 'Kierownik.WAURL_Pobierz_URL_Produktow()',
                                         Kierownik.numer_wyjatku, url=url)

        poczatek = self.zrodlo_strony.find('_ordarticleslistportlet_WAR_ordebusinessfrontapp_-list')
        koniec = self.zrodlo_strony.find('Footer article')
        html = self.zrodlo_strony[poczatek:koniec]

            # przejście do kolejnego pojedynczego produktu
        url_produktow = []
        while 'class="span4 blocArticle"' in html:

            numer = html.find('class="span4 blocArticle"')
            html = html[numer:-1]

            numer = html.find('href="') + 6
            html = html[numer:-1]

            koniec = html.find('"')
            url_produktow.append('https://www.deltaplus.eu' +
                                 html[0:koniec])

        return url_produktow


    def Wczytaj_Adresy_URL(self):

            # wczytuje wcześniej wczytane adresy
        if os.path.exists('sql/deltaplus.urls'):
            with open('sql/deltaplus.urls', 'rb') as plik:
                self.adresy_url = pickle.load(plik)

            return

            # wczytuję wszystkie adresy
        self.Pobieranie_Zrodla_Strony('https://www.deltaplus.eu/pl/by-protection/-/navigation/po-produktach/ochrona-glowy/p/ST15/545/0')

            # wycięcie odpowiedniego bloku
        numer = self.zrodlo_strony.find('class="-lvl1 contentmenuTree')
        html = self.zrodlo_strony[numer:-1]

        koniec = html.find('<script')
        html = html[0:koniec]

            # typy produktów
        while '<li class="itemLvl2' in html:

            html, typ = self.WAURL_Pobierz_Nazwe(html, '<li class="itemLvl2')
            self.adresy_url[typ] = {}

                # dziedziny produktów
            html_typ = html[0:html.find('<li class="itemLvl2')]
            while '<li class="itemLvl3' in html_typ:

                html_typ, dziedzina = self.WAURL_Pobierz_Nazwe(html_typ, '<li class="itemLvl3')
                self.adresy_url[typ][dziedzina] = {}

                    # rodzaje produktów
                html_dziedzina = html_typ[0:html_typ.find('<li class="itemLvl3')]
                while '<li class="itemLvl4' in html_dziedzina:

                    adres_url = self.WAURL_Pobierz_URL_Rodzaj(html_dziedzina)
                    html_dziedzina, rodzaj = self.WAURL_Pobierz_Nazwe(html_dziedzina, '<li class="itemLvl4')

                        # zapisuję listę adresów url produktów
                    self.adresy_url[typ][dziedzina][rodzaj] = \
                        self.WAURL_Pobierz_URL_Produktow('https://www.deltaplus.eu' + adres_url)


    def Zapisz_Adresy_URL(self):
        if not os.path.exists('sql/deltaplus.urls'):
            with open('sql/deltaplus.urls', 'wb') as plik:
                pickle.dump(self.adresy_url, plik, pickle.HIGHEST_PROTOCOL)


    def Pobieranie_Zrodla_Strony(self, url, nacisnij_link=None):

            # pobieranie źródła
        self.firefox.get(url)
        time.sleep(2) # oczekuje załadowania strony

            # naciśnięcie na link (event)
        if nacisnij_link:
            link = self.firefox.find_element_by_link_text(nacisnij_link)
            link.click()
            time.sleep(4)

            # zamknięcie przeglądarki
        self.zrodlo_strony = self.firefox.page_source


    def Dodaj_Produkt_Do_Bazy_Danych(self, url, typ, dziedzina,
                                     rodzaj, pickler):

        if Kierownik.odczyt_produktow: # odczytuję produkty z istniejącego pliku
            produkt = pickler.load()

                # zapisywanie
            Baza_Danych(produkt, typ, dziedzina)

        else:

            self.Pobieranie_Zrodla_Strony(url)
            konwerter = Konwerter(self.zrodlo_strony, rodzaj)

                # zapisywanie
            pickler.dump(konwerter.produkt)
            Baza_Danych(konwerter.produkt, typ, dziedzina)


    def __init__(self):

            # ustawienia przeglądarki
        binary = FirefoxBinary('/home/endo93/Firefox 46.0/firefox')
        self.firefox = webdriver.Firefox(firefox_binary=binary)
        os.system('rm sql/deltaplus.log')

        self.Wczytaj_Adresy_URL()
        self.Zapisz_Adresy_URL()

            # pickler - zapis/odczyt produktów z pliku
        pickler = None
        plik = None

        if os.path.exists('sql/deltaplus.prod'):
            Kierownik.odczyt_produktow = True
            plik = open('sql/deltaplus.prod', 'rb')
            pickler = pickle.Unpickler(plik)

        else: # do zapisywania
            plik = open('sql/deltaplus.prod', 'wb')
            pickler = pickle.Pickler(plik, pickle.HIGHEST_PROTOCOL)

            # dla każdego adresu url
        for typ in self.adresy_url:
            for dziedzina in self.adresy_url[typ]:
                for rodzaj in self.adresy_url[typ][dziedzina]:
                    for url in self.adresy_url[typ][dziedzina][rodzaj]:
                        self.Dodaj_Produkt_Do_Bazy_Danych(url, typ, dziedzina,
                                                          rodzaj, pickler)

        plik.close()
        self.firefox.close()




Kierownik()
