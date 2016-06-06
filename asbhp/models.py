# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class CSS(models.Model):

    klasa = models.CharField(max_length=20)

    def __str__(self):
        return self.klasa.encode('utf8')


class Start(models.Model):

    zawartosc = models.TextField()
    css = models.ForeignKey(CSS, on_delete=models.CASCADE)

    def __str__(self):
        return self.zawartosc.encode('utf8')


class O_Firmie(models.Model):

    zawartosc = models.TextField()
    css = models.ForeignKey(CSS, on_delete=models.CASCADE)

    def __str__(self):
        return self.zawartosc.encode('utf8')


class Oferta(models.Model):

    zawartosc = models.TextField()
    css = models.ForeignKey(CSS, on_delete=models.CASCADE)

    def __str__(self):
        return self.zawartosc.encode('utf8')


class Kontakt(models.Model):

    zawartosc = models.TextField()
    css = models.ForeignKey(CSS, on_delete=models.CASCADE)

    def __str__(self):
        return self.zawartosc.encode('utf8')
