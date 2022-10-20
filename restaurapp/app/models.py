from random import choices
from django.db import models

# Carta
class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
   
    def _str_(self):
        return self.nombre

class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
   
    def _str_(self):
        return self.nombre

# Cliente
class Mesa(models.Model):
    numero = models.IntegerField()
    plato = models.ForeignKey(Plato, on_delete=models.PROTECT)
    bebida = models.ForeignKey(Bebida, on_delete=models.PROTECT)
    hora_pedido = models.TimeField()
    descripcion = models.TextField()

    
    def _str_(self):
        return self.numero

# BODEGA
class Marca(models.Model):
    nombre = models.CharField(max_length=50)
   
    def _str_(self):
        return self.nombre

class Destribuidor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.EmailField()
   
    def _str_(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    destribuidor = models.ForeignKey(Destribuidor, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    fecha_fabricacion = models.DateField()
    fecha_vencimiento = models.DateField()

    def _str_(self):
        return self.nombre

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


    def _str_(self):
        return self.nombre