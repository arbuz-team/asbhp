# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meta_Tagi',
            fields=[
                ('adres_strony', models.URLField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=155)),
                ('og_type', models.CharField(max_length=100)),
                ('og_url', models.CharField(max_length=200)),
                ('og_image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Zawartosc_Zakladki',
            fields=[
                ('zakladka', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('tytul', models.CharField(max_length=200)),
                ('tekst', models.TextField()),
            ],
        ),
    ]
