from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('profesionales/', prof, name="profesionales"),
    path('mant/profesional/agregar/', agregar_profesional , name="agregar_profesional"),
    path('listar_profesionales/', listar_profesionales, name="listar_profesionales"),
    path('modificar_profesional/<rut>/', modificar_profesional, name="modificar_profesional"),
    path('eliminar_profesional/<rut>/', eliminar_profesional, name="eliminar_profesional"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('registro_profesional/', registro_profesional, name="reg_prof"),
    path('registrar_atencion/', registrar_atencion, name="reg_atencion")

]
