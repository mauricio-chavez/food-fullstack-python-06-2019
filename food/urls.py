"""food URL Configuration"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('users.urls', 'users'), namespace='users')),
    path('donuts/', include(('donuts.urls', 'donuts'), namespace='donuts')),
    path('tacos/', include(('tacos.urls', 'tacos'), namespace='tacos')),
    path('api-auth/', include('rest_framework.urls')),
]
