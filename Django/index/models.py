from django.db import models

class index(models.Model):
    user_id = models.PositiveIntegerField(max_length=12)
    stage = models.CharField(max_length=12)
    
    index_Spark = models.PositiveIntegerField(max_length=3)
    index_Labo = models.PositiveIntegerField(max_length=3)
    index_Nexia = models.PositiveIntegerField(max_length=3)
    index_Cobalt = models.PositiveIntegerField(max_length=3)
    index_Gentra = models.PositiveIntegerField(max_length=3)
    index_Lacetti = models.PositiveIntegerField(max_length=3)
    index_Malibu = models.PositiveIntegerField(max_length=3)
    index_Malibu2 = models.PositiveIntegerField(max_length=3)
    index_Equinox = models.PositiveIntegerField(max_length=3)
    index_Monza = models.PositiveIntegerField(max_length=3)
    index_Onix = models.PositiveIntegerField(max_length=3)
    index_Tracker = models.PositiveIntegerField(max_length=3)
    index_Matiz = models.PositiveIntegerField(max_length=3)
      