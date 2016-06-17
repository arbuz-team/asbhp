from django.conf.urls import url, include

urlpatterns = [
    url(r'^uzytkownik/', include('uzytkownik.urls')),
    url(r'^wyszukiwarka/', include('wyszukiwarka.urls')),
    url(r'^produkt/', include('produkt.urls')),
    url(r'^komunikat/', include('komunikat.urls')),
    url(r'^dodatek/', include('dodatek.urls')),
    url(r'', include('asbhp.urls')),
]
