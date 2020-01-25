"""food URL Configuration"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('donuts/', include(('donuts.urls', 'donuts'), namespace='donuts')),
]
