from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def carta(request):
    return render(request, 'app/carta.html')

def bodega(request):
    producto = Producto.objects.all()
    data = {
        'producto': producto
    }
    return render(request, 'app/carta.html', data)
