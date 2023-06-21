from django.urls import path
from .views import *

urlpatterns = [
    path('principal/', principal, name="principal"),
    path('', principal, name="principal"),
    path('contacto/',contacto,name="contacto"),
    path('servicio/',servicio,name="servicio"),
    path('sesion/', sesion, name= "sesion"),
    path('pagfrenos/',pagfrenos,name="pagfrenos"),
    path('pagbujias/',pagbujias,name="pagbujias"),
    path('pagscanner/',pagscanner,name="pagscanner"),
    path('categoria/',categoria,name="categoria"),
    path('loginadministrador/',loginadministrador,name="loginadministrador"),
    path('loginmecanico/',loginmecanico,name="loginmecanico"),
    path('loginprincipal/',loginprincipal,name="loginprincipal"),
    path('pagmecanicos/',pagmecanicos,name="pagmecanicos"),
    path('perfilMecCamila/',perfilMecCamila,name="perfilMecCamila"),
    path('perfilmecSofia/',perfilmecSofia,name="perfilmecSofia"),
    path('perfilMecPamela/',perfilMecPamela,name="perfilMecPamela"),
    path('perfilmecJuan/',perfilmecJuan,name="perfilmecJuan"),
    path('perfilMecMario/',perfilMecMario,name="perfilMecMario"),
    path('perfilMecPedro/',perfilMecPedro,name="perfilMecPedro"),
    path('mantencionkilo/',mantencionkilo,name="mantencionkilo"),
    path('mantencionbateria/',mantencionbateria,name="mantencionbateria"),
    path('mantencionfreno/',mantencionfreno,name="mantencionfreno"),
    path('mantencionbateria/',mantencionbateria,name="mantencionbateria"),
    path('mantenimientoscanner/',mantenimientoscanner,name="mantenimientoscanner"),
    path('mantencionotros/',mantencionotros,name="mantencionotros"),
    path('loginmecanico/',loginmecanico,name="loginmecanico"),
    path('loginadministrador/',loginadministrador,name="loginadministrador"),
    path('loginusuario/',loginusuario,name="loginusuario"),
    path('formularioRegistroAtencion/',formularioRegistroAtencion,name="formularioRegistroAtencion"),
    path('tareasadministrador/',tareasadministrador,name="tareasadministrador"),
   

    
    


]
