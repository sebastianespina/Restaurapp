from django.urls import path
from.views import home,carta


urlpatterns = [
    path('', home, name="home"),
    path('carta/', carta, name="carta"),
    path('bodega/', carta, name="bodega"),
]