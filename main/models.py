from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    sword = models.CharField(max_length=255)
    bow = models.CharField(max_length=255)
    armor = models.CharField(max_length=255)
    description = models.TextField()
# Create your models here.
