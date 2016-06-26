# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models



class Zawartosc_Zakladki(models.Model):

    zakladka = models.CharField(max_length=10, primary_key=True)
    tytul = models.CharField(max_length=200)
    tekst = models.TextField()




class Meta_Tagi(models.Model):

    adres_strony = models.URLField(primary_key=True)
    description = models.CharField(max_length=155)

    og_type = models.CharField(max_length=100)
    og_url = models.CharField(max_length=200)
    og_image = models.CharField(max_length=200)

    def __str__(self):
        return self.adres_strony.encode('utf8')
