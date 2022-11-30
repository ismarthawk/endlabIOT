from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name + str(self.price)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_on = models.DateField(default=timezone.now)
    status = models.CharField(max_length=200, default='Ordered')
