from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=3,max_digits=1000)
    description = models.TextField()