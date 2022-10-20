from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm
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




def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save
            data['mensaje'] = "contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)


def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html',data)

def listar_producto(request):  
    producto = Producto.objects.all()

    data = {
        'producto': producto
    }

    return render(request, 'app/producto/listar.html',data)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        data["form"]= formulario

    return render(request, 'app/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_producto")