from django.contrib import admin
from .models import Plato, Bebida, Mesa, Marca, Destribuidor, Producto

# Register your models here.

admin.site.register(Plato)
admin.site.register(Bebida)
admin.site.register(Mesa)
admin.site.register(Marca)
admin.site.register(Destribuidor)
admin.site.register(Producto)