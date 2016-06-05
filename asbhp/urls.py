from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.Start, name='Start'),
    url(r'^o_firmie/$', views.O_Firmie, name='O_Firmie'),
    url(r'^oferta/$', views.Oferta, name='Oferta'),
    url(r'^kontakt/$', views.Kontakt, name='Kontakt'),

]
