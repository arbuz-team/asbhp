from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wyszukaj/', include('wyszukiwarka.urls')),
    url(r'', include('asbhp.urls')),
]
