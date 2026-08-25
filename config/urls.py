from django.contrib import admin
from django.urls import path

from core.views import inicio, acerca, contacto, estudiantes, profesores

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio, name="inicio"),
    path("acerca/", acerca, name="acerca"),
    path("contacto/", contacto, name="contacto"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("profesores/", profesores, name="profesores"),

]