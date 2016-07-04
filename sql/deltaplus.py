# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from dodatek.views import *
import time



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
        pass


    def Pobierz_Rozmiar(self):

        numer = self.html.find('<section class="groupingRules"')
        rozmiar = self.html[numer:-1]

        numer = rozmiar.find('rozmiar')
        rozmiar = rozmiar[numer:-1]

        poczatek = rozmiar.find('<p>') + 3
        koniec = rozmiar.find('</p>')

        self.produkt['rozmiar'] = \
            rozmiar[poczatek:koniec].translate(None, '\t\n')


    def Pobierz_Producent(self):
        self.produkt['producent'] = 'DeltaPlus'


    def Pobierz_Kolor(self):

        numer = self.html.find('<section class="groupingRules"')
        kolor = self.html[numer:-1]

        numer = kolor.find('KOLOR')
        kolor = kolor[numer:-1]

        poczatek = kolor.find('<p>') + 3
        koniec = kolor.find('</p>')

        self.produkt['kolor'] = \
            kolor[poczatek:koniec].translate(None, '\t\n\xe2\x80\x8b')


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
                    translate(None, '\t\n').split('\xc2\xa0')[0:2])


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


    def __init__(self, html, rodzaj):

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
        self.Pobierz_Slowa_Kluczowe()
        self.Pobierz_Rozmiar()
        self.Pobierz_Producent()
        self.Pobierz_Kolor()
        self.Pobierz_Rodzaj(rodzaj)
        self.Pobierz_Certyfikaty()
        self.Pobierz_Zagrozenia()
        self.Pobierz_Zawody()
        self.Pobierz_Zdjecie()




class Baza_Danych:

    produkt = {}


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

        for zagrozenia in self.produkt['zagrozenia']:
            if not Zagrozenie.objects.filter(nazwa=zagrozenia):
                Zagrozenie.objects.create(nazwa=zagrozenia).save()

        for zawody in self.produkt['zawody']:
            if not Zawod.objects.filter(nazwa=zawody):
                Zawod.objects.create(nazwa=zawody).save()


    def Konwertuj_MTM(self): # ManyToMany

        certyfikaty = self.produkt['certyfikaty']
        self.produkt['certyfikaty'] = \
                [Certyfikat.objects.get(numer=c[0]) for c in certyfikaty]

        zagrozenia = self.produkt['zagrozenia']
        self.produkt['zagrozenia'] = \
            [Zagrozenie.objects.get(nazwa=z) for z in zagrozenia]

        zawody = self.produkt['zawody']
        self.produkt['zawody'] = \
            [Zawod.objects.get(nazwa=z) for z in zawody]


    def Dodaj_Produkt(self):
        produkt = Produkt.objects.create(
            nazwa=self.produkt['nazwa'],
            opis=self.produkt['opis'],
            slowa_kluczowe=self.produkt['slowa_kluczowe'],
            rozmiar=self.produkt['rozmiar'],
            producent=Producent.objects.get(nazwa=self.produkt['producent']),
            kolor=Kolor.objects.get(nazwa=self.produkt['kolor']),
            rodzaj=Rodzaj_Odziezy.objects.get(nazwa=self.produkt['rodzaj'])
        )

        produkt.save()

            # certyfikaty, zagrożenia, zawody
        for c in self.produkt['certyfikaty']:
            produkt.certyfikaty.add(c)

        for z in self.produkt['zagrozenia']:
            produkt.zagrozenia.add(z)

        for z in self.produkt['zawody']:
            produkt.zawody.add(z)

            # zdjęcie
        produkt.Zapisz_Zdjecie_URL(self.produkt['zdjecie'])


    def __init__(self, produkt, typ, dziedzina):
        self.produkt = produkt

        self.Sprawdz_Podklasy(typ, dziedzina)
        self.Konwertuj_MTM()
        self.Dodaj_Produkt()





class Kierownik:

    adresy_url = {} # {typ: {dziedzina: {rodzaj: [adresy_url]}}, ...}
    zrodlo_strony = ''


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

            # wczytanie źródła strony z naciśniętym linkiem '48'
        self.Pobieranie_Zrodla_Strony(url, '48')

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


    def Pobieranie_Zrodla_Strony(self, url, nacisnij_link=None):

            # ustawienia przeglądarki
        binary = FirefoxBinary('/home/endo93/Firefox 46.0/firefox')
        driver = webdriver.Firefox(firefox_binary=binary)

            # pobieranie źródła
        driver.get(url)
        time.sleep(2) # oczekuje załadowania strony

            # naciśnięcie na link (event)
        if nacisnij_link:
            link = driver.find_element_by_link_text(nacisnij_link)
            link.click()
            time.sleep(5)

            # zamknięcie przeglądarki
        self.zrodlo_strony = driver.page_source.encode('utf-8')
        driver.close()


    def Dodaj_Produkt_Do_Bazy_Danych(self, url, typ, dziedzina, rodzaj):

        self.Pobieranie_Zrodla_Strony(url)
        konwerter = Konwerter(self.zrodlo_strony, rodzaj)
        Baza_Danych(konwerter.produkt, typ, dziedzina)


    def __init__(self):

        self.Wczytaj_Adresy_URL()

            # dla każdego adresu url
        for typ in self.adresy_url:
            for dziedzina in self.adresy_url[typ]:
                for rodzaj in self.adresy_url[typ][dziedzina]:
                    for url in self.adresy_url[typ][dziedzina][rodzaj]:
                        self.Dodaj_Produkt_Do_Bazy_Danych(url, typ, dziedzina, rodzaj)




Kierownik()
