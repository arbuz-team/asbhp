# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from arbuz.settings import *
import os

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
    opis = models.TextField(null=True)
    slowa_kluczowe = models.TextField(null=True)
    rozmiar = models.CharField(max_length=20, null=True)
    producent = models.ForeignKey(Producent)
    kolor = models.ForeignKey(Kolor)
    rodzaj = models.ForeignKey(Rodzaj_Odziezy, on_delete=models.CASCADE)
    certyfikaty = models.ManyToManyField('Certyfikat')
    zagrozenia = models.ManyToManyField('Zagrozenie')
    zawody = models.ManyToManyField('Zawod')
    zdjecie = models.FileField()

    def Ustaw_Nazwe_Zdjecia(self):
        rozszerzenie = os.path.splitext(self.zdjecie.name)[1]
        nowa_nazwa = '/static/img/produkt/{0}{1}'\
            .format(self.pk, rozszerzenie)

        stara_nazwa = MEDIA_ROOT + '/{0}'\
            .format(os.path.basename(self.zdjecie.name))

        os.rename(stara_nazwa, BASE_DIR + nowa_nazwa)
        self.zdjecie.name = nowa_nazwa
        self.save()

    def __str__(self):
        return self.nazwa.encode('utf8')


class Dodatek(models.Model):

    numer = models.IntegerField()
    opis = models.TextField()
    rodzaj = models.ForeignKey(Rodzaj_Odziezy, on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE)

    def __str__(self):
        return self.opis.encode('utf8')


################## Promowanie ##################

class Polecane(models.Model):

    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    data_zakonczenia = models.DateField()

    def __str__(self):
        return str(self.produkt)