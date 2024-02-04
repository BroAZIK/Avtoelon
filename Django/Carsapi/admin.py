from django.contrib import admin
from .models import *

modeling = [Spark, Labo, Nexia, Cobalt, Gentra, Lacetti, Malibu, Malibu2, Equinox, Monza, Onix, Tracker, Matiz]
admin.site.register(modeling)
