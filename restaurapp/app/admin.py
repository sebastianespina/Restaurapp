from django.contrib import admin
from .models import Plato, Bebida, Mesa, Marca, Destribuidor, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
   list_display = ["nombre", "precio", "marca", "destribuidor", "cantidad", "fecha_fabricacion", "fecha_vencimiento"] # muestra los campos sin que se tenga que apretar el producto
   list_editable = ["precio"] #edita los campos sin que se tenga que apretar el producto 
   search_fields = ["nombre", "precio"] # se puede buscar por estos campos en el buscador todos los que considan
   list_filter = ["marca", "destribuidor"] # crea un filtro de los distintas marcas y destribidoras para una busqueda mejor

admin.site.register(Plato)
admin.site.register(Bebida)
admin.site.register(Mesa)
admin.site.register(Marca)
admin.site.register(Destribuidor)
admin.site.register(Producto,ProductoAdmin)