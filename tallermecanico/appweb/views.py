from django.shortcuts import render, redirect, get_object_or_404
from .models import Mecanico,Atencion,list_categoria,Cargo,Categoria,Contacto,Postulante
from .forms import ContactoForm, MecanicoForm, AtencionForm,PostulanteForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime
from django.views.generic import ListView
import logging


logger = logging.getLogger(__name__)
# Create your views here.
def principal(request):
    return render(request, "principal.html")

def contacto(request):
    data ={
        'form' :  ContactoForm, 
        'mensaje':""
    }
   
    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "El contacto se ha guardado"
        else:
            data["mensaje"] = "Ha ocurrido un error!!!"
            data["form"] = formulario

    return render(request, "contacto.html", data)



@login_required(login_url='/accounts/login')
@permission_required(['appweb.view_profesional'], login_url='/accounts/login')
def tareasadministrador(request):
    return render(request, "tareasadministrador.html")




def agregar_mecanico(request):
    data= {
        'form': MecanicoForm,
        'mensaje':""
    }
    if request.method == "POST":
        formulario = MecanicoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "El profesional se ha guardado"
        else:
            data["mensaje"] = "Hubo un error"
            data["form"] = formulario

    return render(request, "mantenedor/profesional/agregar.html", data)



def listar_mecanicos(request):
    mecanico = Mecanico.objects.all()
    data = {
        "pagmecanicos" : mecanico
    }
    return render(request, "mantenedor/profesional/listar.html", data)



    
def modificar_mecanico(request,rut):

    mecanico = get_object_or_404(Mecanico, rut=rut)

    data = {
        "form": MecanicoForm(instance=mecanico)
    }
    if request.method == 'POST':
        formulario = MecanicoForm(data=request.POST, files=request.FILES, instance=mecanico)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_mecanicos")
        else:
            data["mensaje"] = "Hubo un error"
            data["form"] =  formulario


    return render(request, "mantenedor/profesional/modificar.html",data)



def eliminar_mecanico(request, rut):
    mecanico = get_object_or_404(Mecanico, rut=rut)

    mecanico.delete()
    messages.success(request, "El profesional rut: "+ rut + " fue eliminado correctamente")
    return redirect(to="listar_mecanicos")

  
def login_usuario(request):
    print("Bienvenido "+ request.user.username)


    print("Grupos", request.user.groups.all())

    if request.user.groups.filter(name='mecanico'):
        print("Es un mecanico")

    return redirect(to='principal')



def registro_mecanico(request):
    data = {
        "mensaje": ""
    }
    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            data["mensaje"] = "Las contraseñas deben ser iguales"
        else:
            usu = User()
            usu.set_password(password1)
            usu.email = correo
            usu.username = nombre
            usu.first_name = nombre
            usu.last_name = apellido
            grupo = Group.objects.get(name='mecanico')
            try:
                usu.save()
                usu.groups.add(grupo)
                data["mensaje"] = "Usuario creado"
                user = authenticate(username=usu.username, password=password1)
                login(request, user)
                return redirect(to='principal')
            except:
                data["mensaje"] = "Error"
    return render(request, "registration/registro.html", data)




@login_required(login_url='/accounts/login')
@permission_required(['appweb.view_atencion'], login_url='/accounts/login')
def tareasMecanico(request):
    return render(request, "tareasMecanico.html")

@login_required(login_url='/accounts/login')
def registrar_atencion(request):
    data= {
        'form': AtencionForm,
        'mensaje':""
    }
    if request.method == "POST":
        formulario = AtencionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            atencion = formulario.save(commit=False)
            atencion.usuario = request.user
            formulario.save()
            data["mensaje"] = "La atencion se ha registrado"
        else:
            data["mensaje"] = "Hubo un error"
            data["form"] = formulario
  
    return render(request, "atencion.html",data)







def lista_atencion(request):
    aten = Atencion.objects.filter(Estado='Pendiente')
    data = {
        "aten" : aten
    }
    print(data)
    return render(request, "lista_atencion.html",data)



def aprobar_atencion(request, id_atencion):
    atencion = get_object_or_404(Atencion, id_atencion=id_atencion)
    atencion.Estado='Aprobada'
    atencion.save()
    messages.success(request, "La publicacion del usuario fue aprobada correctamente")
    return redirect(to="lista_atencion")

def lista_atenciones_aprobadas(request):
    aten=None
    id_cat=request.GET.get('id_cat', '')
    if id_cat != '':
        aten = Atencion.objects.filter(Estado='Aprobada',categoria=id_cat)
    else:
        aten = Atencion.objects.filter(Estado='Aprobada')
    data = {
        "aten" : aten,
        "list_categoria":list_categoria
    }
    return render(request, "atencionesAprobadas.html",data)


def eliminar_atencion(request, id_atencion):
    motivo_rechazo=request.GET.get('motivo_rechazo', '')
    atencion = get_object_or_404(Atencion, id_atencion=id_atencion)
    atencion.Estado='Rechazada'
    atencion.motivoRechazo=motivo_rechazo

    atencion.save()
    messages.success(request, "Rechazada")
    return redirect(to="lista_atencion")

@login_required(login_url='/accounts/login')
def lista_atencion_rechazada(request):
    usuario_logueado = request.user
    
    pendientes = Atencion.objects.filter(Estado='Pendiente', usuario=usuario_logueado)
    rechazado = Atencion.objects.filter(Estado='Rechazada', usuario=usuario_logueado)
    
    data = {
        "rechazado": rechazado,
        "pendientes": pendientes
    }
    print(data)
    return render(request, "atencionesRechazadas.html", data)


def modificar_atencion(request,id_atencion):

    atencion = get_object_or_404(Atencion, id_atencion=id_atencion)
    atencion.Estado='Rechazada'

    data = {
        "form": AtencionForm(instance=atencion)
    }
    if request.method == 'POST':
        formulario = AtencionForm(data=request.POST, files=request.FILES, instance=atencion)
        if formulario.is_valid():
            atencion.Estado='Pendiente'
            formulario.save()
            return redirect(to="lista_atencion_rechazada")
        else:
            data["mensaje"] = "Hubo un error"
            data["form"] =  formulario


    return render(request, "modificarAtencion.html",data)


def Inform_atenciones(request,id_atencion):
    atencion = Atencion.objects.filter(id_atencion=id_atencion)
    data = {
        "atencion" : atencion
    }
    print(data)
    return render(request, "informacion_atencion.html",data)

def Inform_mecanico(request,id_mecanico):
    mecanico = Mecanico.objects.filter(id_mecanico=id_mecanico)
    data = {
        "mecanico" : mecanico
    }
    print(data)
    return render(request, "informacion_mecanico.html",data)

def listar_contacto(request):
    contactos = Contacto.objects.all()
    data = {
        "contactos" : contactos
    }
    return render(request, "lista_contacto.html", data)


def servicio(request):
    return render(request, "servicio.html")

def sesion(request):
    return render(request, "sesion.html")

def pagfrenos(request):
    return render(request, "pagfrenos.html")

def pagbujias(request):
    return render(request, "pagbujias.html")

def pagscanner(request):
    return render(request, "pagscanner.html")

def vistaPrevia(request):
    atenciones = Atencion.objects.all()
   #creamos un objeto para enviar al template
    data={
       'atenciones':atenciones 
   }
    
    return render(request, "vistaPrevia.html",data)

def pagscanner(request):
    return render(request, "pagscanner.html")

def pagmecanicos(request):
    mecanicos = None
    nombreCargo = request.GET.get('nom_cargo', '')
    cargos = Cargo.objects.all()

    if nombreCargo != '':
        mecanicos = Mecanico.objects.filter(cargo__nombre=nombreCargo)
    else:
        mecanicos = Mecanico.objects.all()

    data = {
        'mecanicos': mecanicos,
        'cargos': cargos,
        'nombreCargo': nombreCargo
    }

    return render(request, "pagmecanicos.html", data)

def busquedaAtenciones(request):
    
    text = request.GET.get('search_text', '')
    categoria=Categoria.objects.filter(nombre_categoria__contains=text).last()
    print(categoria)
    aten = Atencion.objects.filter(Estado='Aprobada',categoria=categoria)
    data = {
        "aten" : aten
    }

    return render(request, "resultado_atenciones.html", data)

def registrar_postulante(request):
    data= {
        'form': PostulanteForm,
        'mensaje':""
    }
    if request.method == "POST":
        formulario = PostulanteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "La atencion se ha registrado"
        else:
            data["mensaje"] = "Hubo un error"
            data["form"] = formulario
  
    return render(request, "formulario_postulante.html",data)

def lista_postulante(request):
    postulantes = Postulante.objects.all()
    data = {
        "postulantes" : postulantes
    }
    print(data)
    return render(request, "lista_postulante.html",data)

def Inform_postulante(request,id_postulante):
    postulantes = Postulante.objects.filter(id_postulante=id_postulante)
    data = {
        "postulantes" : postulantes
    }
    print(data)
    return render(request, "informacion_postulante.html",data)


def eliminar_postulante(request, id_postulante):
    postulante = get_object_or_404(Postulante, id_postulante=id_postulante)

    postulante.delete()
    messages.success(request, " postulante eliminado correctamente")
    return redirect(to="lista_postulante")




