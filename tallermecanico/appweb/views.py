from django.shortcuts import render, redirect, get_object_or_404
from .models import Mecanico,Atencion
from .forms import ContactoForm, MecanicoForm, AtencionForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime

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
@permission_required(['appweb.view_mecanico'], login_url='/accounts/login')
def registrar_atencion(request):
    data= {
        'form': AtencionForm,
        'mensaje':""
    }
    if request.method == "POST":
        formulario = AtencionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "La atencion se ha registrado"
        else:
            data["mensaje"] = "Hubo un error"
            data["form"] = formulario
  
    return render(request, "atencion.html",data)


def lista_atencion(request):
    aten = Atencion.objects.all()
    data = {
        "aten" : aten
    }
    
    return render(request, "lista_atencion.html",data)


def eliminar_atencion(request, observacion):
    atencion = get_object_or_404(Atencion, observacion=observacion)

    atencion.delete()
    messages.success(request, "La publicacion del usuario: "+ observacion + " fue eliminada correctamente")
    return redirect(to="lista_atencion")

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

def categoria(request):
    return render(request, "categoria.html")

def loginadministrador(request):
    return render(request, "loginadministrador.html")

def loginmecanico(request):
    return render(request, "loginmecanico.html")

def loginprincipal(request):

    return render(request, "loginprincipal.html")

def vistaPrevia(request):
    atenciones = Atencion.objects.all()
   #creamos un objeto para enviar al template
    data={
       'atenciones':atenciones 
   }
    
    return render(request, "vistaPrevia.html",data)

def pagscanner(request):
    return render(request, "pagscanner.html")

def mantencionbateria(request):
    return render(request, "mantencionbateria.html")

def mantencionfreno(request):
    return render(request, "mantencionfreno.html")

def mantencionkilo(request):
    return render(request, "mantencionkilo.html")

def mantencionotros(request):
    return render(request, "mantencionotros.html")

def mantenimientoscanner(request):
    return render(request, "mantenimientoscanner.html")

def pagmecanicos(request):
    #se crea una variable llamada mecanicos
    mecanicos = Mecanico.objects.all()
   #creamos un objeto para enviar al template
    data={
       'mecanicos':mecanicos 
   }

    return render(request, "pagmecanicos.html", data)




def adminAtencion(request):
    return render(request, "adminAtencion.html")

def adminMecanico(request):
    return render(request, "adminMecanico.html")

def formularioRegistroAtencion(request):
    return render(request, "formularioRegistroAtencion.html")
