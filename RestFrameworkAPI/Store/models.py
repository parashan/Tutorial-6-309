from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    stock_count = models.IntegerField()
    price = models.FloatField()
    picture = models.ImageField(upload_to="Images", null=True)