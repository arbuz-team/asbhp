#! /usr/bin/fish
rm db.sqlite3
rm asbhp/migrations/*
rm uzytkownik/migrations/*
rm produkt/migrations/*

python manage.py makemigrations asbhp
python manage.py makemigrations uzytkownik
python manage.py makemigrations produkt

python manage.py migrate auth

python manage.py migrate asbhp
python manage.py migrate uzytkownik
python manage.py migrate produkt

chmod 777 db.sqlite3
