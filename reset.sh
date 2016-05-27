#! /bin/bash
rm db.sqlite3
rm asbhp/migrations/*
python manage.py makemigrations asbhp
python manage.py migrate auth
python manage.py migrate asbhp
chmod 777 db.sqlite3
