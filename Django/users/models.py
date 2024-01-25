from django.db import models

class users(models.Model):
    user_id = models.PositiveIntegerField(max_length=12)

    first = models.CharField(max_length=32)
    last  = models.CharField(max_length=32)


