from django import forms
from .models import Contacto,Mecanico,Atencion


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"
        #fields = ["nombre", "email", "mensaje"]


class MecanicoForm(forms.ModelForm):

    class Meta: 
        model = Mecanico
        fields = "__all__"

        widgets = {
            "fecha_nacimiento": forms.DateTimeInput(attrs={'type':'date'}, format=('%Y-%m-%d'))
        }


class AtencionForm(forms.ModelForm):

    class Meta: 
        model = Atencion
        fields = "__all__"

        

        widgets = {
            'motivoRechazo': forms.HiddenInput(),
            'Estado': forms.HiddenInput(),
            "fecha": forms.DateTimeInput(attrs={'type':'date'}, format=('%Y-%m-%d'))
            
        }