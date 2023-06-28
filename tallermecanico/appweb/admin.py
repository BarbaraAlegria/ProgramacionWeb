from django.contrib import admin
from .models import *

# Register your models here.
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido']
    list_editable = ['apellido']
    list_filter = ['cargo']
    
    search_fields = ['rut']

admin.site.register(Cargo)
admin.site.register(Mecanico, MecanicoAdmin)
admin.site.register(Contacto)
admin.site.register(Atencion)


