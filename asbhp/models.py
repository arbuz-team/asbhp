# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Zakladka(models.Model):

    nazwa_url = models.CharField(max_length=50)
    nazwa = models.CharField(max_length=50)
    zawartosc_html = models.TextField()
    zawartosc = models.TextField()

    def __str__(self):
        return self.nazwa


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


class Kolor(models.Model):

    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa


class Opis(models.Model):

    opis = models.TextField()

    def __str__(self):
        return self.nazwa


class Firma(models.Model):

    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa


class Produkt(models.Model):

    nazwa = models.CharField(max_length=50)
    opis = models.ForeignKey('Opis')
    firma = models.ForeignKey('Firma')
    kolor = models.ForeignKey('Kolor')
    id_rodzaj = models.ForeignKey('Rodzaj_Odziezy',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa




#class Certyfikat(models.Model):
#
#    nazwa = models.CharField(max_length=50)
#
#    def __str__(self):
#        return self.nazwa