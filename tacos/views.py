"""Tacos app views"""

from rest_framework import viewsets

from .models import Taco, Tortilla
from .serializers import TacoSerializer, TortillaSerializer


class TacoViewSet(viewsets.ModelViewSet):
    queryset = Taco.objects.all()
    serializer_class = TacoSerializer


class TortillaViewSet(viewsets.ModelViewSet):
    queryset = Tortilla.objects.all()
    serializer_class = TortillaSerializer
