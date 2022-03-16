from django.db import models

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=32, default="Blank") 
    description = models.CharField(max_length=255, default="Blank")
    price = models.IntegerField(max_length=32, default=0)
    rarity = models.CharField(max_length=32, default="Blank")
    condition = models.CharField(max_length=255, default="Blank")