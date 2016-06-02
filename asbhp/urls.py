from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Start, name='Start'),
    url(r'^o_firmie/$', views.O_Firmie, name='O_Firmie'),
    url(r'^oferta/$', views.Oferta, name='Oferta'),
    url(r'^kontakt/$', views.Kontakt, name='Kontakt'),

    url(r'^produkt/(?P<pk>\d)/$', views.Wyswietl_Produkt, name='Wyswietl_Produkt'),

    url(r'^dodaj/produkt/$', views.Dodaj_Produkt, name='Dodaj_Produkt'),
    url(r'^dodaj/firma/$', views.Dodaj_Firma, name='Dodaj_Firma'),
    url(r'^dodaj/kolor/$', views.Dodaj_Kolor, name='Dodaj_Kolor'),
    url(r'^dodaj/certyfikat/$', views.Dodaj_Certyfikat, name='Dodaj_Certyfikat'),
    url(r'^dodaj/dodatek/$', views.Dodaj_Dodatek, name='Dodaj_Dodatek'),
    url(r'^dodaj/polecane/$', views.Dodaj_Polecane, name='Dodaj_Polecane'),

    url(r'^usun/produkt/(?P<pk>\d)/$', views.Usun_Produkt, name='Usun_Produkt'),
    url(r'^usun/firma/(?P<pk>\d)/$', views.Usun_Firma, name='Usun_Firma'),
    url(r'^usun/kolor/(?P<pk>\d)/$', views.Usun_Kolor, name='Usun_Kolor'),
    url(r'^usun/certyfikat/(?P<pk>\d)/$', views.Usun_Certyfikat, name='Usun_Certyfikat'),
    url(r'^usun/dodatek/(?P<pk>\d)/$', views.Usun_Dodatek, name='Usun_Dodatek'),
    url(r'^usun/polecane/(?P<pk>\d)/$', views.Usun_Polecane, name='Usun_Polecane'),

    url(r'^edytuj/produkt/(?P<pk>\d)/$', views.Edytuj_Produkt, name='Edytuj_Produkt'),
]
