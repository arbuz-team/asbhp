# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uzytkownicy',
            fields=[
                ('login', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('haslo', models.CharField(max_length=200)),
            ],
        ),
    ]
