from random import choices
from django.db import models

# Carta
class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
   
    def __str__(self):
        return self.nombre

class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
   
    def __str__(self):
        return self.nombre

# Cliente
class Mesa(models.Model):
    numero = models.IntegerField()
    plato = models.ForeignKey(Plato, on_delete=models.PROTECT)
    bebida = models.ForeignKey(Bebida, on_delete=models.PROTECT)
    hora_pedido = models.TimeField()
    descripcion = models.TextField()

    
    def __str__(self):
        return self.numero

# BODEGA
class Marca(models.Model):
    nombre = models.CharField(max_length=50)
   
    def __str__(self):
        return self.nombre

class Distribuidor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.EmailField()
   
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    fecha_fabricacion = models.DateField()
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.nombre

    def line_total(self):
        return self.cantidad * self.precio

#  imagen = models.ImageField(upload_to="producto", null=True)


#Contacto
opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipoconsulta = models.IntegerField(choices=opciones_consultas)
    mensaje =  models.TextField()
    avisos = models.BooleanField()


    def __str__(self):
        return self.nombre