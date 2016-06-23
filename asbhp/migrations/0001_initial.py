# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-23 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kontakt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zawartosc', models.TextField()),
                ('przeznaczenie', models.CharField(max_length=20)),
            ],
        ),
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
            name='O_Firmie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zawartosc', models.TextField()),
                ('przeznaczenie', models.CharField(max_length=20)),
            ],
        ),
    ]
