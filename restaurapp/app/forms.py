from django import forms
from .models import  Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields =  ["consulta","reclamo","sugerencia","felicitaciones"]
        fields = '__all__'