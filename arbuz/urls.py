from django.conf.urls import url, include

urlpatterns = [
    url(r'^uzytkownik/', include('uzytkownik.urls')),
    url(r'^wyszukiwarka/', include('wyszukiwarka.urls')),
    url(r'^produkt/', include('produkt.urls')),
    url(r'', include('asbhp.urls')),
]
