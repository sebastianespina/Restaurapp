from django import forms
from .models import  Contacto, Producto

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
            

        
        
