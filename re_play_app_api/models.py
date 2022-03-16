from django.db import models

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    price = models.IntegerField(max_length=32)
    rarity = models.CharField(max_length=32)
    condition = models.CharField(max_length=255)