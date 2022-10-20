from django import forms
from .models import  Contacto, Producto
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields =  ["consulta","reclamo","sugerencia","felicitaciones"]
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget(),
            "fecha_vencimiento": forms.SelectDateWidget()
        }
            
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "password1", "password2"]
        
        
