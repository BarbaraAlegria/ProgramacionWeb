from django.contrib import admin
from .models import *

# Register your models here.

class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'especialista']
    list_editable = ['apellido']
    list_filter = ['cargo']
    
    search_fields = ['rut']

class AtencionAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'monto', 'Modelo', 'categoria','observacion']
    
    
    
    search_fields = ['observacion']

admin.site.register(Cargo)
admin.site.register(Profesional, ProfesionalAdmin)
admin.site.register(Contacto)
admin.site.register(Atencion,AtencionAdmin)
