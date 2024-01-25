# serializers.py
from rest_framework import serializers
from .models import *

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # Bu qiymatga alohida modelni kiritishingiz kerak
        fields = '__all__'

class SparkSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Spark

class LaboSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Labo

class DamasSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Damas

class NexiaSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Nexia

class CobaltSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Cobalt

class GentraSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Gentra

class LacettiSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Lacetti

class MalibuSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Malibu

class Malibu2Serializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Malibu

class EquinoxSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Equinox

class MonzaSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Monza

class MatizSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Matiz

class OnixSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Onix

class TrackerSerializer(CarSerializer):
    class Meta(CarSerializer.Meta):
        model = Tracker
