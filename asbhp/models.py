# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


################## Główne ##################

class Zakladka(models.Model):

    nazwa_url = models.CharField(max_length=50)
    nazwa = models.CharField(max_length=50)
    zawartosc_html = models.TextField()
    zawartosc = models.TextField()

    def __str__(self):
        return self.nazwa


################## Produkt: Kontenery ##################

class Typ_Odziezy(models.Model):

    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa


class Dziedzina_Odziezy(models.Model):

    nazwa = models.CharField(max_length=100)
    id_typ = models.ForeignKey('Typ_Odziezy',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa


class Rodzaj_Odziezy(models.Model):

    nazwa = models.CharField(max_length=100)
    id_dziedzina = models.ForeignKey('Dziedzina_Odziezy',
                                     on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa


################## Produkt: Produkty ##################

class Opis(models.Model):

    numer = models.IntegerField()
    opis = models.TextField()

    def __str__(self):
        return self.numer


class Firma(models.Model):

    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa


class Kolor(models.Model):

    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa


class Certyfikat(models.Model):

    numer = models.CharField(max_length=20)
    szczegoly = models.CharField(max_length=50)

    def __str__(self):
        return self.numer


class Zagrozenie(models.Model):

    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa


class Zawod(models.Model):

    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa


class Produkt(models.Model):

    nazwa = models.CharField(max_length=50)
    opis = models.ForeignKey('Opis')
    firma = models.ForeignKey('Firma')
    kolor = models.ForeignKey('Kolor')
    rozmiar = models.CharField(max_length=20)
    waga = models.IntegerField() # gramy
    sztuk = models.IntegerField()
    id_rodzaj = models.ForeignKey('Rodzaj_Odziezy',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa


class Dodatek(models.Model):

    numer = models.IntegerField()
    opis = models.TextField()
    id_rodzaj = models.ForeignKey('Rodzaj_Odziezy', on_delete=models.CASCADE)
    id_firmy = models.ForeignKey('Firma', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_rodzaj + self.id_firmy


################## Produkt: Łączenie ##################

class Certyfikaty_Dla_Produktu(models.Model):

    id_produktu = models.ForeignKey('Produkt', on_delete=models.CASCADE)
    id_certyfikatu = models.ForeignKey('Certyfikat', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('id_produktu', 'id_certyfikatu'),)


class Zagrozenia_Dla_Produktu(models.Model):

    id_produktu = models.ForeignKey('Produkt', on_delete=models.CASCADE)
    id_zagrozenia = models.ForeignKey('Zagrozenie', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('id_produktu', 'id_zagrozenia'),)

class Zawody_Dla_Produktu(models.Model):

    id_produktu = models.ForeignKey('Produkt', on_delete=models.CASCADE)
    id_zawodu = models.ForeignKey('Zawod', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('id_produktu', 'id_zawodu'),)
