from django.db import models

class Product(models.Model):
    name = models.TextField(default="book")
    price = models.TextField(default="5000")
    description = models.TextField(default="great product")