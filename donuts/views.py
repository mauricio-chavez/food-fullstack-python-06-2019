"""Donuts app views"""

from django.shortcuts import render

from .models import Donut


def index(request):
    """Donuts index"""
    context = {
        'donuts': Donut.objects.all()
    }
    return render(request, 'donuts/index.html', context)
