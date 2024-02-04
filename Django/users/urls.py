from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('all/', Usersview.as_view()),
    path('alt/<int:pk>/', UserDetailView.as_view()),
    ]