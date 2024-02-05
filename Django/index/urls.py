from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Indexview.as_view()),
    path('<int:pk>/<str:mk>/', Indexdetailview.as_view())
    ]