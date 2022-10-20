from django.urls import path
from.views import home, carta, bodega, contacto, agregar_producto, listar_producto, modificar_producto, eliminar_producto


urlpatterns = [
    path('', home, name="home"),
    path('carta/', carta, name="carta"),
    path('bodega/', bodega, name="bodega"),
    path('contacto/', contacto, name="contacto"),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('listar_producto/', listar_producto, name="listar_producto"),
    path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
]