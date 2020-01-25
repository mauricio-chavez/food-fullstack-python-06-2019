"""Donuts app views"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Donut


@login_required
def index(request):
    """Donuts index"""
    context = {
        'donuts': Donut.objects.all()
    }
    return render(request, 'donuts/index.html', context)
