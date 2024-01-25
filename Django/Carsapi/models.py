from django.db import models

class Spark(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"

class Labo(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"

class Damas(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"

class Nexia(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        f"{self.price}$ - {self.title}"

class Cobalt(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"

class Gentra(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"

class Lacetti(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"

class Malibu(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"

class Malibu2(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"

class Equinox(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"
    
class Monza(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"

class Matiz(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"

class Onix(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"
    
class Tracker(models.Model):
    price  = models.CharField(max_length=10)
    url    = models.CharField(max_length=60)
    title  = models.CharField(max_length=32)
    detail = models.CharField(max_length=64)
    more   = models.CharField(max_length=120)
    images = models.CharField(max_length=256)
    lot    = models.CharField(max_length=64)

    avto   = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.price}$ - {self.title}"
    
      

