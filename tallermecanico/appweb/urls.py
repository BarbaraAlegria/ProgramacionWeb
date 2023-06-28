from django.urls import path
from .views import *

urlpatterns = [
    path('principal/', principal, name="principal"),
    path('', principal, name="principal"),
    path('contacto/',contacto,name="contacto"),
    path('pagmecanicos/',pagmecanicos,name="pagmecanicos"),
    path('mantenedor/profesional/agregar/', agregar_mecanico , name="agregar_mecanico"),
    path('mantenedor/profesional/listar/', listar_mecanicos , name="listar_mecanicos"),
    path('mantenedor/profesional/modificar/<rut>/', modificar_mecanico, name="modificar_mecanico"),
    path('eliminar_profesional/<rut>/', eliminar_mecanico, name="eliminar_mecanico"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('registro_profesional/', registro_mecanico, name="registro_mecanico"),
    path('atencion/', registrar_atencion, name="atencion"),
    path('sesion/', sesion, name= "sesion"),
    path('vistaPrevia/',vistaPrevia,name="vistaPrevia"),
    path('lista_atencion/',lista_atencion,name="lista_atencion"),
    path('eliminar_atencion/<observacion>/', eliminar_atencion, name="eliminar_atencion"),



    path('servicio/',servicio,name="servicio"),
    
    path('pagfrenos/',pagfrenos,name="pagfrenos"),
    path('pagbujias/',pagbujias,name="pagbujias"),
    path('pagscanner/',pagscanner,name="pagscanner"),
    path('categoria/',categoria,name="categoria"),
    path('loginadministrador/',loginadministrador,name="loginadministrador"),
    path('loginmecanico/',loginmecanico,name="loginmecanico"),
    path('loginprincipal/',loginprincipal,name="loginprincipal"),
    path('pagmecanicos/',pagmecanicos,name="pagmecanicos"),
    
    
    
    path('mantencionkilo/',mantencionkilo,name="mantencionkilo"),
    path('mantencionbateria/',mantencionbateria,name="mantencionbateria"),
    path('mantencionfreno/',mantencionfreno,name="mantencionfreno"),
    path('mantencionbateria/',mantencionbateria,name="mantencionbateria"),
    path('mantenimientoscanner/',mantenimientoscanner,name="mantenimientoscanner"),
    path('mantencionotros/',mantencionotros,name="mantencionotros"),
    path('loginmecanico/',loginmecanico,name="loginmecanico"),
    path('loginadministrador/',loginadministrador,name="loginadministrador"),
    
    path('formularioRegistroAtencion/',formularioRegistroAtencion,name="formularioRegistroAtencion"),
    path('tareasadministrador/',tareasadministrador,name="tareasadministrador"),
    
   

    
    


]
