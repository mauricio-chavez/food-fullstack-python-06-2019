"""Tacos app serializers"""

from rest_framework import serializers

from .models import Taco, Tortilla


class TortillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tortilla
        fields = '__all__'


class TacoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taco
        fields = '__all__'
