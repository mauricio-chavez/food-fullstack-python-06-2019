"""Users app views"""

# Stardard library

# Django
from django.contrib.auth import (
    authenticate, login as signin, logout as signout
)
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Third Party
from rest_framework import viewsets

# Local
from .forms import UserForm
from .serializers import UserSerializer


# Class based View REST Framework

from rest_framework.views import APIView
from rest_framework.response import Response


class Example(APIView):
    def post(self, request, format=None):
        data = {
            'message': 'Hello REST',
        } 
        return Response(data)


# Class based View Django

from django.views.generic import View
from django.http import JsonResponse

class ExampleDjango(View):
    def post(self, request):
        data = {
            'message': 'Hello REST',
        } 
        return JsonResponse(data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request=request, username=username, password=password
        )
        if user:
            signin(request, user)
            return redirect('donuts:index')
        else:
            context['error'] = 'Credenciales incorrectas'

    return render(request, 'users/login.html', context)


def logout(request):
    signout(request)
    messages.success(request, 'Has cerrado sesión correctamente')
    return redirect('users:login')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            signin(request, user)
            return redirect('donuts:index')
    else:
        form = UserForm()

    return render(request, 'users/signup.html', {'form': form})
