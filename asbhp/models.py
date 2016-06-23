# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class O_Firmie(models.Model):

    zawartosc = models.TextField()
    przeznaczenie = models.CharField(max_length=20)

    def __str__(self):
        return self.przeznaczenie.encode('utf8')


class Kontakt(models.Model):

    zawartosc = models.TextField()
    przeznaczenie = models.CharField(max_length=20)

    def __str__(self):
        return self.przeznaczenie.encode('utf8')


class Meta_Tagi(models.Model):

    adres_strony = models.URLField(primary_key=True)
    description = models.CharField(max_length=155)

    og_type = models.CharField(max_length=100)
    og_url = models.CharField(max_length=200)
    og_image = models.CharField(max_length=200)

    def __str__(self):
        return self.adres_strony.encode('utf8')
