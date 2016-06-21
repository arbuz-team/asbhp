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
