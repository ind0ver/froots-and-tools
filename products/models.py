from django.db import models

# Create your models here.


class Broduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    category = models.SmallIntegerField()


class Woffer(models.Model):
    code = models.CharField(max_length=8)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
