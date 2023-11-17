from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.TextField()
    type = models.CharField(max_length=255, null=True)
    rarity= models.CharField(max_length=255, null=True)
    is_discount = models.BooleanField(default=False)
# Create your models here.
