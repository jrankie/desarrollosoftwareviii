from django.contrib import admin
from django.urls import path

from core.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio, name="inicio"),
    path("acerca/", acerca, name="acerca"),
    path('estudiantes/', estudiantes, name='estudiantes'),
]