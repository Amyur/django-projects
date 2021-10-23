from django.http import HttpResponse
import datetime
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): # Esta es una vista. La primera vista
    p1 = Persona("Lau", "Urrea")

    ctx = {"nombre_mio":p1.nombre, "apellido_mio":p1.apellido, "temas":["python", "sql", "SAS"]}

    return(render(request, "plantilla.html", ctx))

def Padre_Hija(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "HijaC.html", {"Dame_Fecha":fecha_actual})

def Padre_HijaA(request):

    return render(request, "HijaA.html")

def dame_fecha(request):

    fecha_actual = datetime.datetime.now()

    documento = """ <html>
    <body>
    <h1>
    La fecha actual es: %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return(HttpResponse(documento))
    
def calculaEdad(request, ano):
    edad_actual = 23
    periodo = ano - 2021
    edad_futura = edad_actual + periodo
    documento = "<html><body><h1>Mi edad en el año %s será de %s" % (ano, edad_futura)

    return(HttpResponse(documento))