# -*- coding: utf-8 -*-
from produkt.models import *

################## Zagrożenie ##################
Zagrozenie.objects.create(nazwa='Antyelektrostatyczność').save()
Zagrozenie.objects.create(nazwa='Hałas').save()
Zagrozenie.objects.create(nazwa='Ciepło').save()
Zagrozenie.objects.create(nazwa='Uderzenie').save()
Zagrozenie.objects.create(nazwa='Upadek').save()
Zagrozenie.objects.create(nazwa='Przecięcie / przekłucie').save()
Zagrozenie.objects.create(nazwa='Zimno / niepogoda').save()
Zagrozenie.objects.create(nazwa='Poślizg').save()
Zagrozenie.objects.create(nazwa='Cząstki biologiczne, chemiczne').save()
Zagrozenie.objects.create(nazwa='Zużycie').save()
Zagrozenie.objects.create(nazwa='UV / IR').save()
Zagrozenie.objects.create(nazwa='Elektryczność').save()
Zagrozenie.objects.create(nazwa='Słaba widoczność').save()

################## Zawód ##################
Zawod.objects.create(nazwa='Rolnictwo / ogrodnictwo').save()
Zawod.objects.create(nazwa='Budownictwo / roboty publiczne').save()
Zawod.objects.create(nazwa='Prace remontowe / Rzemiosło').save()
Zawod.objects.create(nazwa='Przemysł ciężki').save()
Zawod.objects.create(nazwa='Przemysł lekki').save()
Zawod.objects.create(nazwa='Usługi / logistyka').save()
Zawod.objects.create(nazwa='Służba zdrowia / żywienie zbiorowe').save()
Zawod.objects.create(nazwa='Przemysł petrochemiczny / gazowniczy').save()
Zawod.objects.create(nazwa='Górnictwo').save()
Zawod.objects.create(nazwa='Ergetyka wiatrowa ').save()
