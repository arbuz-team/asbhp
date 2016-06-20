from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^wyslij/$', views.Wyslij_Email, name='Wyslij_Email'),
    url(r'^wybierz_temat/$', views.Wybierz_Temat, name='Wybierz_Temat'),
    url(r'^pytanie_o_produkt/$', views.Pytanie_O_Produkt, name='Pytanie_O_Produkt'),
    url(r'^uwagi_www/$', views.Uwagi_WWW, name='Uwagi_WWW'),
    url(r'^inny_temat/$', views.Inny_Temat, name='Inny_Temat'),

]
