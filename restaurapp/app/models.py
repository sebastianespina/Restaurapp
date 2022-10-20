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

# MESERO
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
    correo = models.TextField()
   
    def _str_(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    destribuidor = models.ForeignKey(Destribuidor, ondelete=models.PROTECT)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    fecha_fabricacion = models.DateField()
    fecha_vencimiento = models.DateField()

    def _str_(self):
        return self.nombre

