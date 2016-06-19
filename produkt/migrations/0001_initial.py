# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-19 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certyfikat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numer', models.CharField(max_length=20)),
                ('szczegoly', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dodatek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numer', models.IntegerField()),
                ('opis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Dziedzina_Odziezy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kolor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Polecane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_zakonczenia', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Producent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('opis', models.TextField()),
                ('slowa_kluczowe', models.TextField(blank=True, null=True)),
                ('rozmiar', models.CharField(blank=True, max_length=20, null=True)),
                ('zdjecie', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('certyfikaty', models.ManyToManyField(blank=True, to='produkt.Certyfikat')),
                ('kolor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Kolor')),
                ('producent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Producent')),
            ],
        ),
        migrations.CreateModel(
            name='Rodzaj_Odziezy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('dziedzina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Dziedzina_Odziezy')),
            ],
        ),
        migrations.CreateModel(
            name='Typ_Odziezy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Zagrozenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Zawod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='produkt',
            name='rodzaj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Rodzaj_Odziezy'),
        ),
        migrations.AddField(
            model_name='produkt',
            name='zagrozenia',
            field=models.ManyToManyField(blank=True, to='produkt.Zagrozenie'),
        ),
        migrations.AddField(
            model_name='produkt',
            name='zawody',
            field=models.ManyToManyField(blank=True, to='produkt.Zawod'),
        ),
        migrations.AddField(
            model_name='polecane',
            name='produkt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Produkt'),
        ),
        migrations.AddField(
            model_name='dziedzina_odziezy',
            name='typ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Typ_Odziezy'),
        ),
        migrations.AddField(
            model_name='dodatek',
            name='producent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Producent'),
        ),
        migrations.AddField(
            model_name='dodatek',
            name='rodzaj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Rodzaj_Odziezy'),
        ),
    ]
