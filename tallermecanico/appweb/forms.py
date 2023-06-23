from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"
        #fields = ["nombre", "email", "mensaje"]
