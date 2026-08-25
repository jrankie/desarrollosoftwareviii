from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse


def inicio(request):
    return HttpResponse(
        "<h1>Desarrollo de Software VIII</h1>"
        "<p>Mi primer proyecto Django está funcionando correctamente.</p>"
    )

def acerca(request):
    return HttpResponse(
        "<h1>Acerca del proyecto</h1>"
        "<p>Proyecto desarrollado para Desarrollo de Software VIII.</p>"
        "<p>Grupo: 2GS131</p>"
    )