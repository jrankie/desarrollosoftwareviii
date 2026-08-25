from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return HttpResponse(
        "<h1>Desarrollo de Software VIII</h1>"
        "<p>Mi primer proyecto Django está funcionando correctamente.</p>"
        "<a href='/estudiantes/'>Estudiantes</a><br>"
        "<a href='/acerca/'>Acerca del proyecto</a>"
    )


def acerca(request):
    return HttpResponse(
        "<h1>Acerca del proyecto</h1>"
        "<p>Proyecto desarrollado para Desarrollo de Software VIII.</p>"
        "<p>Grupo: 2GS131</p>"
    )


def estudiantes(request):
    return HttpResponse(
        "<h1>Estudiantes</h1>"
        "<p>Lista de estudiantes del grupo 2GS131.</p>"
    )