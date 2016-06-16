from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^logowanie/$', views.Logowanie, name='Logowanie'),
    url(r'^rejestracja/$', views.Rejestracja, name='Rejestracja'),
    url(r'^wyloguj/$', views.Wyloguj, name='Wyloguj'),

]
