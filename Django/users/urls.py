from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Usersview.as_view()),
    ]