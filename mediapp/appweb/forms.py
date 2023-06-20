from django import forms
from .models import Contacto, Profesional

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"
        #fields = ["nombre", "email", "mensaje"]

class ProfesionalForm(forms.ModelForm):

    class Meta: 
        model = Profesional
        fields = "__all__"

        widgets = {
            "fecha_nacimiento": forms.DateTimeInput(attrs={'type':'date'}, format=('%Y-%m-%d'))
        }


