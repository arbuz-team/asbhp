from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^(?P<pk>\d+)/$', views.Wyswietl_Produkt, name='Wyswietl_Produkt'),

    url(r'^dodaj/$', views.Dodaj_Produkt, name='Dodaj_Produkt'),
    url(r'^dodaj/producent/$', views.Dodaj_Producent, name='Dodaj_Producent'),
    url(r'^dodaj/kolor/$', views.Dodaj_Kolor, name='Dodaj_Kolor'),
    url(r'^dodaj/certyfikat/$', views.Dodaj_Certyfikat, name='Dodaj_Certyfikat'),
    url(r'^dodaj/dodatek/$', views.Dodaj_Dodatek, name='Dodaj_Dodatek'),
    url(r'^dodaj/polecane/$', views.Dodaj_Polecane, name='Dodaj_Polecane'),

    url(r'^usun/(?P<pk>\d+)/$', views.Usun_Produkt, name='Usun_Produkt'),
    url(r'^usun/producent/(?P<pk>\d+)/$', views.Usun_Producent, name='Usun_Producent'),
    url(r'^usun/kolor/(?P<pk>\d+)/$', views.Usun_Kolor, name='Usun_Kolor'),
    url(r'^usun/certyfikat/(?P<pk>\d+)/$', views.Usun_Certyfikat, name='Usun_Certyfikat'),
    url(r'^usun/dodatek/(?P<pk>\d+)/$', views.Usun_Dodatek, name='Usun_Dodatek'),
    url(r'^usun/polecane/(?P<pk>\d+)/$', views.Usun_Polecane, name='Usun_Polecane'),

    url(r'^edytuj/(?P<pk>\d+)/$', views.Edytuj_Produkt, name='Edytuj_Produkt'),

]
