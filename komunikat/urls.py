from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^404/$', views.Wyswietl_404, name='Wyswietl_404'),
    url(r'^potwierdzenie/$', views.Wyswietl_Potwierdzenie,
        name='Wyswietl_Potwierdzenie'),

]