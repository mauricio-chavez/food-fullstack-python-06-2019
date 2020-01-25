"""Donuts app model"""

from django.db import models


class Donut(models.Model):
    """Donut model"""
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name + ' - $' + str(self.price)
