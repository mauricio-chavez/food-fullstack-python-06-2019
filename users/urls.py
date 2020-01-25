"""Users urls"""

from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('users/', include(router.urls)),

    path('example', views.Example.as_view()),
    path('example-django', views.ExampleDjango.as_view()),

]
