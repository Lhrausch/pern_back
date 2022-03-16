from django.db import models

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=32, default="Blank", editable=True) 
    description = models.CharField(max_length=255, default="Blank", editable=True)
    price = models.IntegerField(max_length=32, default=0, editable=True)
    rarity = models.CharField(max_length=32, default="Blank", editable=True)
    condition = models.CharField(max_length=255, default="Blank", editable=True)