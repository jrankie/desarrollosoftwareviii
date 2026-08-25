from django.contrib import admin
from django.urls import path

from core.views import inicio, acerca

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio, name="inicio"),
    path("acerca/", acerca, name="acerca"),
]