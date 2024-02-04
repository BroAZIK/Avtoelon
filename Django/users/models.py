from django.db import models

class users(models.Model):
    user_id = models.IntegerField(unique=True)


    first = models.CharField(max_length=32)
    last  = models.CharField(max_length=32) 
    
    def __str__(self):
        return f"{self.first} {self.last}"