from django.urls import path
from .views import *

urlpatterns = [
    path('principal/', principal, name="principal"),
    path('', principal, name="principal"),
    path('contacto/',contacto,name="contacto"),
    path('servicio/',servicio,name="servicio"),
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
    path('eliminar_atencion/<id_atencion>/', eliminar_atencion, name="eliminar_atencion"),
    path('aprobar_atencion/<id_atencion>/', aprobar_atencion, name="aprobar_atencion"),
    path('atencionesAprobadas/', lista_atenciones_aprobadas, name="lista_atenciones_aprobadas"),
    path('servicio/',servicio,name="servicio"),
    path('pagfrenos/',pagfrenos,name="pagfrenos"),
    path('pagbujias/',pagbujias,name="pagbujias"),
    path('pagscanner/',pagscanner,name="pagscanner"),
    path('pagmecanicos/',pagmecanicos,name="pagmecanicos"),
    path('tareasadministrador/',tareasadministrador,name="tareasadministrador"),
    path('tareasMecanico/',tareasMecanico,name="tareasMecanico"),
    path('atencionesRechazadas/',lista_atencion_rechazada,name="lista_atencion_rechazada"),
    path('modificarAtencion/<id_atencion>/',modificar_atencion,name="modificar_atencion"),
    path('lista_contacto/',listar_contacto,name="listar_contacto"),
    path('formulario_postulante/',registrar_postulante,name="registrar_postulante"),
    path('lista_postulante/',lista_postulante,name="lista_postulante"),
    path('informacion_postulante/<id_postulante>/',Inform_postulante,name="Inform_postulante"),
    path('eliminar_postulante/<id_postulante>/', eliminar_postulante, name="eliminar_postulante"),
    path('informacion_atencion/<id_atencion>/',Inform_atenciones,name="Inform_atenciones"),
    path('informacion_mecanico/<id_mecanico>/',Inform_mecanico,name="Inform_mecanico"),
    path('busqueda_atenciones/',busquedaAtenciones,name="busqueda_atenciones"),
    
]
    



