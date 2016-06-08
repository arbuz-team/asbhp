from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.Wyszukaj, name='Wyszukaj'),
    url(r'^usun_sesje/$', views.Usun_Sesje, name='Usun_Sesje'),

    url(r'^producent/$', views.Filtr_Producent, name='Filtr_Producent'),
    url(r'^kolor/$', views.Filtr_Kolor, name='Filtr_Kolor'),
    url(r'^zagrozenia/$', views.Filtr_Zagrozenia, name='Filtr_Zagrozenia'),
    url(r'^zawody/$', views.Filtr_Zawody, name='Filtr_Zawody'),

    url(r'^typ/$', views.Kontener_Typ, name='Kontener_Typ'),
    url(r'^dziedzina/$', views.Kontener_Dziedzina, name='Kontener_Dziedzina'),
    url(r'^rodzaj/$', views.Kontener_Rodzaj, name='Kontener_Rodzaj'),

]
