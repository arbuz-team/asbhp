from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wyszukiwarka/', include('wyszukiwarka.urls')),
    url(r'^produkt/', include('produkt.urls')),
    url(r'', include('asbhp.urls')),
]
