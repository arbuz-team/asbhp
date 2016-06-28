# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from arbuz.settings import *
from PIL import Image
import os, cStringIO, urllib



################## Produkt: Kontenery ##################

class Typ_Odziezy(models.Model):

    nazwa = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa.encode('utf8')




class Dziedzina_Odziezy(models.Model):

    nazwa = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    typ = models.ForeignKey(Typ_Odziezy, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa.encode('utf8')




class Rodzaj_Odziezy(models.Model):

    nazwa = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    dziedzina = models.ForeignKey(Dziedzina_Odziezy, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa.encode('utf8')




################## Produkt: Produkty ##################

class Producent(models.Model):

    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa.encode('utf8')




class Kolor(models.Model):

    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa.encode('utf8')




class Certyfikat(models.Model):

    numer = models.CharField(max_length=20)
    szczegoly = models.CharField(max_length=50)

    def __str__(self):
        return self.numer.encode('utf8')




class Zagrozenie(models.Model):

    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa.encode('utf8')




class Zawod(models.Model):

    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa.encode('utf8')




class Produkt(models.Model):

    nazwa = models.CharField(max_length=50)
    opis = models.TextField()
    slowa_kluczowe = models.TextField(null=True, blank=True)
    rozmiar = models.CharField(max_length=20, null=True, blank=True)
    producent = models.ForeignKey(Producent)
    kolor = models.ForeignKey(Kolor)
    rodzaj = models.ForeignKey(Rodzaj_Odziezy, on_delete=models.CASCADE)
    certyfikaty = models.ManyToManyField('Certyfikat', blank=True)
    zagrozenia = models.ManyToManyField('Zagrozenie', blank=True)
    zawody = models.ManyToManyField('Zawod', blank=True)
    zdjecie = models.ImageField(null=True, blank=True)

    def Zapisz_Zdjecie_Formularz(self):
        rozszerzenie = os.path.splitext(self.zdjecie.name)[1]
        nowa_nazwa = '/static/img/produkt/{0}{1}'\
            .format(self.pk, rozszerzenie)

        stara_nazwa = MEDIA_ROOT + '/{0}'\
            .format(os.path.basename(self.zdjecie.name))

        os.rename(stara_nazwa, BASE_DIR + nowa_nazwa)
        self.zdjecie.name = nowa_nazwa
        self.save()

    def Zapisz_Zdjecie_URL(self, adres_url):
        wejscie = cStringIO.StringIO(urllib.urlopen(adres_url).read())
        obrazek = Image.open(wejscie)
        nowa_nazwa = '/static/img/produkt/{0}.{1}' \
            .format(self.pk, obrazek.format.lower())

        obrazek.save(BASE_DIR + nowa_nazwa)
        self.zdjecie.name = nowa_nazwa
        self.save()

    def __str__(self):
        return self.nazwa.encode('utf8')




################## Promowanie ##################

class Polecane(models.Model):

    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    data_zakonczenia = models.DateField()

    @staticmethod
    def Pobierz_Aktywne_Oferty():
        produkt = []
        for p in Polecane.objects.all():
            if p.data_zakonczenia >= timezone.now().date():
                produkt.append(p)

        return produkt

    @staticmethod
    def Pobierz_Nieaktywne_Oferty():
        produkt = []
        for p in Polecane.objects.all():
            if p.data_zakonczenia < timezone.now().date():
                produkt.append(p)

        return produkt

    def __str__(self):
        return str(self.produkt)
