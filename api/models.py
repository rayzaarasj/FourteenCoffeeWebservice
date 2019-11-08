from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    price = models.IntegerField()
    image_url = models.CharField(max_length=1000, default='')

class Order(models.Model):
    key = models.IntegerField(primary_key=True)
    menus = models.CharField(max_length=500)
    prices = models.CharField(max_length=500)
    counts = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
