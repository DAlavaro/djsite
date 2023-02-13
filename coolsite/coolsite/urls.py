"""coolsite URL Configuration"""

from django.contrib import admin

from women.views import *
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls'))
]

handler404 = pageNotFound
