from django.db import models
# Una clase por tabla
# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="La dirección")
    email = models.EmailField(blank=True, null=True)
    tfono = models.CharField(max_length=7)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    


