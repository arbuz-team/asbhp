# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

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
    produkty = models.ManyToManyField('Produkt', through='Certyfikaty_Dla_Produktu')

    def __str__(self):
        return self.numer.encode('utf8')


class Zagrozenie(models.Model):

    nazwa = models.CharField(max_length=50)
    produkty = models.ManyToManyField('Produkt', through='Zagrozenia_Dla_Produktu')

    def __str__(self):
        return self.nazwa.encode('utf8')


class Zawod(models.Model):

    nazwa = models.CharField(max_length=50)
    produkty = models.ManyToManyField('Produkt', through='Zawody_Dla_Produktu')

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
    certyfikaty = models.ManyToManyField('Certyfikat', through='Certyfikaty_Dla_Produktu')
    zagrozenia = models.ManyToManyField('Zagrozenie', through='Zagrozenia_Dla_Produktu')
    zawody = models.ManyToManyField('Zawod', through='Zawody_Dla_Produktu')

    def __str__(self):
        return self.nazwa.encode('utf8')


class Dodatek(models.Model):

    numer = models.IntegerField()
    opis = models.TextField()
    rodzaj = models.ForeignKey(Rodzaj_Odziezy, on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE)

    def __str__(self):
        return self.opis.encode('utf8')


################## Produkt: Łączenie ##################

class Certyfikaty_Dla_Produktu(models.Model):

    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    certyfikat = models.ForeignKey(Certyfikat, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('produkt', 'certyfikat'),)


class Zagrozenia_Dla_Produktu(models.Model):

    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    zagrozenie = models.ForeignKey(Zagrozenie, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('produkt', 'zagrozenie'),)

class Zawody_Dla_Produktu(models.Model):

    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    zawod = models.ForeignKey(Zawod, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('produkt', 'zawod'),)


################## Promowanie ##################

class Polecane(models.Model):

    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    data_zakonczenia = models.DateField()

    def __str__(self):
        return str(self.produkt)