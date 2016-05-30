from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Start, name='Start'),
    url(r'^o_firmie/$', views.O_Firmie, name='O_Firmie'),
    url(r'^oferta/$', views.Oferta, name='Oferta'),
    url(r'^kontakt/$', views.Kontakt, name='Kontakt'),

    url(r'^produkt/$', views.Lista_Produktow, name='Lista_Produktow'),
    url(r'^produkt/(?P<pk>\d)/$', views.Wyswietl_Produkt, name='Wyswietl_Produkt'),

    url(r'^dodaj/produkt/$', views.Dodaj_Produkt, name='Dodaj_Produkt'),
    url(r'^dodaj/firma/$', views.Dodaj_Firma, name='Dodaj_Firma'),
    url(r'^dodaj/kolor/$', views.Dodaj_Kolor, name='Dodaj_Kolor'),
    url(r'^dodaj/certyfikat/$', views.Dodaj_Certyfikat, name='Dodaj_Certyfikat'),
    url(r'^dodaj/dodatek/$', views.Dodaj_Dodatek, name='Dodaj_Dodatek'),
    url(r'^dodaj/polecane/$', views.Dodaj_Polecane, name='Dodaj_Polecane'),
]
