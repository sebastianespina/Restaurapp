from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
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
            messages.success(request, "Producto regitrado")
            data['mensaje'] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html',data)

def listar_producto(request):  
    producto = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(producto, 5)
        producto = paginator.page(page)
    except:
        raise Http404


    data = {
        'entity': producto,
        'paginator': paginator
    }

    return render(request, 'app/producto/listar.html', data)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_producto")
        data["form"]= formulario

    return render(request, 'app/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_producto")



def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "se a regitrado el usuario correctamente")
            return redirect(to='home')
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)