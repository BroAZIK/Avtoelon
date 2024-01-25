from rest_framework import serializers
from .models import *

class allSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # Bu qiymatga alohida modelni kiritishingiz kerak
        fields = '__all__'

class usersSerializer(allSerializer):
    class Meta(allSerializer.Meta):
        model = users