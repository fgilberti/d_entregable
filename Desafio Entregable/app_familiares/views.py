from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from app_familiares.models import Familiar


def saludo(Request):
    return HttpResponse("Lista de Familiares")


def mostrar_template(Request):
    context = {}

    if Request.GET:
        context["nombre"] = Request.GET["nombre"]
    return render(Request, "app_familiares/index.html", context)


def listar_familiares(Request):
    context = {}
    context["familiares"] = Familiar.objects.all()
    return render(Request, "app_familiares/lista_familiares.html", context)
