# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 00:46
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
            name='Certyfikaty_Dla_Produktu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certyfikat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Certyfikat')),
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
            ],
        ),
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
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
            name='Produkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('opis', models.TextField()),
                ('rozmiar', models.CharField(max_length=20)),
                ('waga', models.IntegerField()),
                ('sztuk', models.IntegerField()),
                ('certyfikaty', models.ManyToManyField(through='produkt.Certyfikaty_Dla_Produktu', to='produkt.Certyfikat')),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Firma')),
                ('kolor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Kolor')),
            ],
        ),
        migrations.CreateModel(
            name='Rodzaj_Odziezy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('dziedzina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Dziedzina_Odziezy')),
            ],
        ),
        migrations.CreateModel(
            name='Typ_Odziezy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Zagrozenia_Dla_Produktu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Produkt')),
            ],
        ),
        migrations.CreateModel(
            name='Zagrozenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('produkty', models.ManyToManyField(through='produkt.Zagrozenia_Dla_Produktu', to='produkt.Produkt')),
            ],
        ),
        migrations.CreateModel(
            name='Zawod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Zawody_Dla_Produktu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Produkt')),
                ('zawod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Zawod')),
            ],
        ),
        migrations.AddField(
            model_name='zawod',
            name='produkty',
            field=models.ManyToManyField(through='produkt.Zawody_Dla_Produktu', to='produkt.Produkt'),
        ),
        migrations.AddField(
            model_name='zagrozenia_dla_produktu',
            name='zagrozenie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Zagrozenie'),
        ),
        migrations.AddField(
            model_name='produkt',
            name='rodzaj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Rodzaj_Odziezy'),
        ),
        migrations.AddField(
            model_name='produkt',
            name='zagrozenia',
            field=models.ManyToManyField(through='produkt.Zagrozenia_Dla_Produktu', to='produkt.Zagrozenie'),
        ),
        migrations.AddField(
            model_name='produkt',
            name='zawody',
            field=models.ManyToManyField(through='produkt.Zawody_Dla_Produktu', to='produkt.Zawod'),
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
            name='firma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Firma'),
        ),
        migrations.AddField(
            model_name='dodatek',
            name='rodzaj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Rodzaj_Odziezy'),
        ),
        migrations.AddField(
            model_name='certyfikaty_dla_produktu',
            name='produkt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produkt.Produkt'),
        ),
        migrations.AddField(
            model_name='certyfikat',
            name='produkty',
            field=models.ManyToManyField(through='produkt.Certyfikaty_Dla_Produktu', to='produkt.Produkt'),
        ),
        migrations.AlterUniqueTogether(
            name='zawody_dla_produktu',
            unique_together=set([('produkt', 'zawod')]),
        ),
        migrations.AlterUniqueTogether(
            name='zagrozenia_dla_produktu',
            unique_together=set([('produkt', 'zagrozenie')]),
        ),
        migrations.AlterUniqueTogether(
            name='certyfikaty_dla_produktu',
            unique_together=set([('produkt', 'certyfikat')]),
        ),
    ]