from __future__ import unicode_literals
from django.db import models

class Uzytkownicy(models.Model):

    login = models.CharField(max_length=50, primary_key=True)
    haslo = models.CharField(max_length=200)

    def __str__(self):
        return self.login.encode('utf8')