from django.urls import path
from.views import home,carta,bodega,contacto


urlpatterns = [
    path('', home, name="home"),
    path('carta/', carta, name="carta"),
    path('bodega/', bodega, name="bodega"),
    path('contacto/', contacto, name="contacto"),
]