from rest_framework import serializers
from .models import *

class allSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # Bu qiymatga alohida modelni kiritishingiz kerak
        fields = '__all__'

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = index
        fields = '__all__'