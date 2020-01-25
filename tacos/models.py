"""Tacos app models"""

from django.db import models

TORTILLA_CHOICES = (
    (1, 'Maíz'),
    (2, 'Maíz azul'),
    (3, 'Harina'),
    (4, 'Taquera'),
    (5, 'Árabe'),
)


class Tortilla(models.Model):
    """Tortilla model"""
    name = models.CharField(max_length=40)
    SIZE_CHOICES = (
        (1, 'Pequeña'),
        (2, 'Mediana'),
        (3, 'Grande'),
    )
    size = models.IntegerField(choices=SIZE_CHOICES)

    def __str__(self):
        return self.name


class Taco(models.Model):
    """Taco model"""
    name = models.CharField(max_length=40)
    price = models.FloatField()
    tortilla = models.ForeignKey(Tortilla, on_delete=models.CASCADE)

    def __str__(self):
        return f'self.name - ${self.price}'
