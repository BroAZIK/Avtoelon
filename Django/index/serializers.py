from rest_framework import serializers
from .models import *

class allSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # Bu qiymatga alohida modelni kiritishingiz kerak
        fields = '__all__'

class IndexSerializer(allSerializer):
    class Meta(allSerializer.Meta):
        model = index