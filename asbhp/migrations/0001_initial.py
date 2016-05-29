# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-29 21:14
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
                ('certyfikat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Certyfikat')),
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
            name='Opis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.TextField()),
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
                ('rozmiar', models.CharField(max_length=20)),
                ('waga', models.IntegerField()),
                ('sztuk', models.IntegerField()),
                ('certyfikaty', models.ManyToManyField(through='asbhp.Certyfikaty_Dla_Produktu', to='asbhp.Certyfikat')),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Firma')),
                ('kolor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Kolor')),
                ('opis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Opis')),
            ],
        ),
        migrations.CreateModel(
            name='Rodzaj_Odziezy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('dziedzina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Dziedzina_Odziezy')),
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
                ('produkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Produkt')),
            ],
        ),
        migrations.CreateModel(
            name='Zagrozenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('produkty', models.ManyToManyField(through='asbhp.Zagrozenia_Dla_Produktu', to='asbhp.Produkt')),
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
                ('produkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Produkt')),
                ('zawod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Zawod')),
            ],
        ),
        migrations.AddField(
            model_name='zawod',
            name='produkty',
            field=models.ManyToManyField(through='asbhp.Zawody_Dla_Produktu', to='asbhp.Produkt'),
        ),
        migrations.AddField(
            model_name='zagrozenia_dla_produktu',
            name='zagrozenie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Zagrozenie'),
        ),
        migrations.AddField(
            model_name='produkt',
            name='rodzaj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Rodzaj_Odziezy'),
        ),
        migrations.AddField(
            model_name='produkt',
            name='zagrozenia',
            field=models.ManyToManyField(through='asbhp.Zagrozenia_Dla_Produktu', to='asbhp.Zagrozenie'),
        ),
        migrations.AddField(
            model_name='produkt',
            name='zawody',
            field=models.ManyToManyField(through='asbhp.Zawody_Dla_Produktu', to='asbhp.Zawod'),
        ),
        migrations.AddField(
            model_name='polecane',
            name='produkt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Produkt'),
        ),
        migrations.AddField(
            model_name='dziedzina_odziezy',
            name='typ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Typ_Odziezy'),
        ),
        migrations.AddField(
            model_name='dodatek',
            name='firma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Firma'),
        ),
        migrations.AddField(
            model_name='dodatek',
            name='rodzaj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Rodzaj_Odziezy'),
        ),
        migrations.AddField(
            model_name='certyfikaty_dla_produktu',
            name='produkt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asbhp.Produkt'),
        ),
        migrations.AddField(
            model_name='certyfikat',
            name='produkty',
            field=models.ManyToManyField(through='asbhp.Certyfikaty_Dla_Produktu', to='asbhp.Produkt'),
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
