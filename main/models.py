from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.TextField()
    type = models.CharField(max_length=255, null=True)
# Create your models here.
