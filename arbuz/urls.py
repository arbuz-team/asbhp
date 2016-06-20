from django.conf.urls import url, include
from django.conf.urls import handler404

urlpatterns = [
    url(r'^uzytkownik/', include('uzytkownik.urls')),
    url(r'^wyszukiwarka/', include('wyszukiwarka.urls')),
    url(r'^produkt/', include('produkt.urls')),
    url(r'^komunikat/', include('komunikat.urls')),
    url(r'^dodatek/', include('dodatek.urls')),
    url(r'^poczta/', include('poczta.urls')),
    url(r'', include('asbhp.urls')),
]

handler404 = 'komunikat.views.Wyswietl_404'