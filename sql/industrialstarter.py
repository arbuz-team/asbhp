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
    os.system('echo "%s" >> sql/industrialstarter.log' % komunikat)




class Konwerter:

    html = ''
    produkt = {}


    def Pobierz_Nazwa(self):

        numer = self.html.find('class="field field-name-title"')
        nazwa = self.html[numer:-1]

        poczatek = nazwa.find('<h1>') + 4
        koniec = nazwa.find('</h1>')

        self.produkt['nazwa'] = \
            nazwa[poczatek:koniec]


    def Pobierz_Opis(self):

        numer = self.html.find('class="field field-name-field-product-description"')
        opis = self.html[numer:-1]

        poczatek = opis.find('>') + 1
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
        pass


    def Pobierz_Producent(self):
        self.produkt['producent'] = 'Industrial Starter'


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

        numer = self.html.find('class="colorbox init-colorbox-processed cboxElement"')
        zdjecie = self.html[numer:-1]

        numer = zdjecie.find('<img ')
        zdjecie = zdjecie[numer:-1]

        poczatek = zdjecie.find('src="') + 5
        koniec = zdjecie.find('.jpg') + 4

        self.produkt['zdjecie'] = zdjecie[poczatek:koniec]


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

        if not Dziedzina_Odziezy.objects.filter(nazwa=dziedzina, typ=Typ_Odziezy.objects.get(nazwa=typ)):
            Dziedzina_Odziezy.objects.create(nazwa=dziedzina,
                                             url=Konwertuj_Nazwe_Na_URL(dziedzina),
                                             typ=Typ_Odziezy.objects.get(nazwa=typ)).save()

        if not Rodzaj_Odziezy.objects.filter(nazwa=self.produkt['rodzaj'],
                                             dziedzina=Dziedzina_Odziezy.objects.get(nazwa=dziedzina, typ=Typ_Odziezy.objects.get(nazwa=typ))):
            Rodzaj_Odziezy.objects.create(nazwa=self.produkt['rodzaj'],
                                          url=Konwertuj_Nazwe_Na_URL(self.produkt['rodzaj']),
                                          dziedzina=Dziedzina_Odziezy.objects.get(nazwa=dziedzina, typ=Typ_Odziezy.objects.get(nazwa=typ))).save()

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

        if not self.produkt['nazwa']:
            return

        self.Sprawdz_Podklasy(typ, dziedzina)
        self.Konwertuj_MTM()

        try:

            self.Dodaj_Produkt(typ, dziedzina)

        except Exception as e:
            Kierownik.numer_wyjatku += 1
            Wyswietl_Komunikat_O_Wyjatku(e, 'Baza_Danych.Dodaj_Produkt()',
                                         Kierownik.numer_wyjatku, self.produkt['nazwa'])




class Kierownik:

    adresy_url = {} # {typ: {dziedzina: {rodzaj: [adresy_url]}}, ...}
    zrodlo_strony = ''
    firefox = None
    numer_wyjatku = 0
    odczyt_produktow = False

    @staticmethod
    def WAURL_Pobierz_Nazwe(html):

        numer = html.find('<a href="') + 9
        html = html[numer + 1:-1]  # "+1" uniknie powtórzeń

        koniec = html.find('">')
        adres = 'http://www.industrialstarter.com/' + html[0:koniec]

        poczatek = koniec + 2
        koniec = html.find('</a>')

            # reszta html, nazwa przycisku, adres przycisku
        return html, html[poczatek:koniec], adres # html się kurczy


    def WAURL_Pobierz_Liste_URL(self, url):

        self.Pobieranie_Zrodla_Strony(url)

            # wycięcie odpowiedniego bloku
        numer = self.zrodlo_strony.find('class="view-content"')
        html = self.zrodlo_strony[numer:-1]

        poczatek = html.find('<ul>')
        koniec = html.find('</ul>')
        html = html[poczatek:koniec]

        adresy = {}

            # zapisywanie nazwy i adresu
        while '<li class="views-row' in html:
            html, nazwa, adres = self.WAURL_Pobierz_Nazwe(html)

            if 'Buty z wysoką cholewą Issa Line' not in nazwa:
                adresy[nazwa] = adres

            # gdy nie znalazł więcej adresów
        if adresy == {}:
            numer = self.zrodlo_strony.find('class="isotope"')
            html = self.zrodlo_strony[numer:-1]
            adresy = []

                # pobieram adresy poszczególnych produktów
            while 'isotope-column' in html:
                numer = html.find('isotope-column')
                html = html[numer + 1:-1] # "+1" unika powtórzeń

                numer = html.find('<a href="')
                html = html[numer:-1]

                poczatek = 9
                koniec = html.find('">')
                adresy.append(html[poczatek:koniec])

        return adresy


    def Wczytaj_Adresy_URL(self):

            # wczytuje wcześniej wczytane adresy
        if os.path.exists('sql/industrialstarter.urls'):
            with open('sql/industrialstarter.urls', 'rb') as plik:
                self.adresy_url = pickle.load(plik)

            return

        self.adresy_url = self.WAURL_Pobierz_Liste_URL('http://www.industrialstarter.com/pl/produkty')

        for typ in self.adresy_url:
            if isinstance(self.adresy_url, dict):
                self.adresy_url[typ] = self.WAURL_Pobierz_Liste_URL(self.adresy_url[typ])

        for typ in self.adresy_url:
            for dziedzina in self.adresy_url[typ]:
                if isinstance(self.adresy_url[typ], dict):
                    self.adresy_url[typ][dziedzina] = \
                        self.WAURL_Pobierz_Liste_URL(self.adresy_url[typ][dziedzina])

        for typ in self.adresy_url:
            print(typ)

            if isinstance(self.adresy_url[typ], dict):
                for dziedzina in self.adresy_url[typ]:
                    print('  ' + str(dziedzina))
                    for elem in self.adresy_url[typ][dziedzina]:
                        print('    ' + str(elem))

            else:
                for elem in self.adresy_url[typ]:
                    print('  ' + str(elem))


    def Zapisz_Adresy_URL(self):
        if not os.path.exists('sql/industrialstarter.urls'):
            with open('sql/industrialstarter.urls', 'wb') as plik:
                pickle.dump(self.adresy_url, plik, pickle.HIGHEST_PROTOCOL)


    def Pobieranie_Zrodla_Strony(self, url, nacisnij_link=None):

            # pobieranie źródła
        self.firefox.get(url)
        #time.sleep(2) # oczekuje załadowania strony

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
        os.system('rm sql/industrialstarter.log')

        self.Wczytaj_Adresy_URL()
        self.Zapisz_Adresy_URL()


            # pickler - zapis/odczyt produktów z pliku
        pickler = None
        plik = None

        if os.path.exists('sql/industrialstarter.prod'):
            Kierownik.odczyt_produktow = True
            plik = open('sql/industrialstarter.prod', 'rb')
            pickler = pickle.Unpickler(plik)

        else: # do zapisywania
            plik = open('sql/industrialstarter.prod', 'wb')
            pickler = pickle.Pickler(plik, pickle.HIGHEST_PROTOCOL)

            # dla każdego adresu url
        for typ in self.adresy_url:

            if isinstance(self.adresy_url[typ], dict):
                for dziedzina in self.adresy_url[typ]:

                    if isinstance(self.adresy_url[typ][dziedzina], dict):
                        print('Huston mamy problem...')

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
