from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm

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