from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('labo/', Laboview.as_view()),
    path('damas/', Damasview.as_view()),
    path('nexia/', Nexiaview.as_view()),
    path('gentra/', Gentraview.as_view()),
    path('cobalt/', Cobaltview.as_view()),
    path('spark/', Sparkview.as_view()),
    path('lacetti/', Lacettiview.as_view()),
    path('malibu/', Malibuview.as_view()),
    path('malibu2/', Malibu2view.as_view()),
    path('equinox/', Equinoxview.as_view()),
    path('monza/', Monzaview.as_view()),
    path('matiz/', Matizview.as_view()),
    path('onix/', Onixview.as_view()),
    path('tracker/', Trackerview.as_view())

]