from django.conf.urls import url
from dodatek.views import *
from . import views


urlpatterns = [

    url(r'^usun_sesje_wyszukiwarki/$', views.Usun_Sesje_Wyszukiwarki,
        name='Usun_Sesje_Wyszukiwarki'),

    url(r'^usun_sesje_filtrow/$', views.Usun_Sesje_Filtrow,
        name='Usun_Sesje_Filtrow'),

    url(r'^$', views.Filtr_Wyszukiwarka_Dla_Oferta, name='Filtr_Wyszukiwarka_Dla_Oferta'),
    url(r'^dla_edytuj/$', views.Filtr_Wyszukiwarka_Dla_Edytuj, name='Filtr_Wyszukiwarka_Dla_Edytuj'),
    url(r'^producent/$', views.Filtr_Producent, name='Filtr_Producent'),
    url(r'^kolor/$', views.Filtr_Kolor, name='Filtr_Kolor'),
    url(r'^zagrozenia/$', views.Filtr_Zagrozenia, name='Filtr_Zagrozenia'),
    url(r'^zawody/$', views.Filtr_Zawody, name='Filtr_Zawody'),
    url(r'^liczba_produktow/$', views.Filtr_Liczba_Produktow, name='Filtr_Liczba_Produktow'),

    url(r'^typ/$', views.Kontener_Typ, name='Kontener_Typ'),
    url(r'^dziedzina/$', views.Kontener_Dziedzina, name='Kontener_Dziedzina'),
    url(r'^rodzaj/$', views.Kontener_Rodzaj, name='Kontener_Rodzaj'),

]
