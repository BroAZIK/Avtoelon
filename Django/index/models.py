from django.db import models

class index(models.Model):
    user_id = models.IntegerField(unique=True)
    stage = models.CharField(max_length=12)
    
    index_Spark = models.IntegerField()
    index_Labo = models.IntegerField()
    index_Nexia = models.IntegerField()
    index_Cobalt = models.IntegerField()
    index_Gentra = models.IntegerField()
    index_Lacetti = models.IntegerField()
    index_Malibu = models.IntegerField()
    index_Malibu2 = models.IntegerField()
    index_Equinox = models.IntegerField()
    index_Monza = models.IntegerField()
    index_Onix = models.IntegerField()
    index_Tracker = models.IntegerField()
    index_Matiz = models.IntegerField()
      