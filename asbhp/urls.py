from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.Wyswietl_Start, name='Wyswietl_Start'),
    url(r'^o_firmie/$', views.Wyswietl_O_Firmie, name='Wyswietl_O_Firmie'),
    url(r'^oferta/$', views.Wyswietl_Oferta, name='Wyswietl_Oferta'),
    url(r'^kontakt/$', views.Wyswietl_Kontakt, name='Wyswietl_Kontakt'),

    url(r'^oferta/(?P<typ_url>\w{0,30})/$',
        views.Wyswietl_Oferta, name='Wyswietl_Oferta'),

    url(r'^oferta/(?P<typ_url>\w{0,30})/(?P<dziedzina_url>\w{0,30})/$',
        views.Wyswietl_Oferta, name='Wyswietl_Oferta'),

    url(r'^oferta/(?P<typ_url>\w{0,30})/(?P<dziedzina_url>\w{0,30})/(?P<rodzaj_url>\w{0,30})/$',
        views.Wyswietl_Oferta, name='Wyswietl_Oferta'),

    url(r'^oferta/(?P<typ_url>\w{0,30})/(?P<dziedzina_url>\w{0,30})/(?P<rodzaj_url>\w{0,30})/(?P<wyszukane_produkty>\w+)/$',
        views.Wyswietl_Oferta, name='Wyswietl_Oferta'),

    url(r'^edytuj/kontakt/$', views.Edytuj_Kontakt, name='Edytuj_Kontakt'),
    url(r'^edytuj/kontakt/(?P<pk>\d)/$', views.Edytuj_Kontakt_Zapisz, name='Edytuj_Kontakt_Zapisz'),

    url(r'^edytuj/o_firmie/$', views.Edytuj_O_Firmie, name='Edytuj_O_Firmie'),
    url(r'^edytuj/o_firmie/(?P<pk>\d)/$', views.Edytuj_O_Firmie_Zapisz, name='Edytuj_O_Firmie_Zapisz'),

]
