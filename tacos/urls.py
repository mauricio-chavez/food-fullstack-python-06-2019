"""Tacos URL config"""

from django.urls import path, include

from rest_framework import routers

from .views import TacoViewSet, TortillaViewSet


router = routers.DefaultRouter()
router.register('tacos', TacoViewSet)
router.register('tortillas', TortillaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
