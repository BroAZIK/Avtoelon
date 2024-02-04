from rest_framework import serializers
from .models import *

class allSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # Bu qiymatga alohida modelni kiritishingiz kerak
        fields = '__all__'

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = "__all__"