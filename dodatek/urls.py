from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^usun_sesje/$', views.Usun_Sesje, name='Usun_Sesje'),

]