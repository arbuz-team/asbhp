from uzytkownik.models import *
from dodatek.views import Szyfruj
Uzytkownicy.objects.create(login='arbuz-team', haslo=Szyfruj('kaktus8')).save()