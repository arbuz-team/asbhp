from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.Wyswietl_Start, name='Wyswietl_Start'),
    url(r'^o_firmie/$', views.Wyswietl_O_Firmie, name='Wyswietl_O_Firmie'),
    url(r'^oferta/$', views.Wyswietl_Oferta, name='Wyswietl_Oferta'),
    url(r'^kontakt/$', views.Wyswietl_Kontakt, name='Wyswietl_Kontakt'),

    url(r'^edytuj/kontakt/$', views.Edytuj_Kontakt, name='Edytuj_Kontakt'),

]
