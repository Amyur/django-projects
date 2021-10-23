from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articulos

# Create your views here.
def busqueda_prod(request):
    return(render(request, "busqueda_productos.html"))

def buscar(request):
    if request.GET["pdr"]:
        #mensaje = "El producto es %r"%request.GET["pdr"]
        producto = request.GET["pdr"]
        articulos = Articulos.objects.filter(nombre__icontains=producto) # es como like de sql
        return(render(request, "resultado_busqueda.html", {"articulos":articulos, "query":producto}))
    else:
        mensaje = "No has introducido un nombre"
        return(HttpResponse(mensaje))