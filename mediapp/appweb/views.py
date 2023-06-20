from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesional, Atencion
from .forms import ContactoForm, ProfesionalForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def home(request):

    request.session["nombre"] = "sebastian"
    request.session["saludo"] = "Bienvenido sebastian"

   # messages.warning(request, "Este es mi primer mensaje")
    return render(request, 'home.html')

def contacto(request):

    data = {
        "form" : ContactoForm
    }

    messages.success(request, request.session["nombre"])


    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "El contacto se ha guardado"
        else:
            data["mensaje"] = "Ha ocurrido un error!!!"
            data["form"] = formulario



    return render(request, 'contacto.html', data)

def prof(request):

    #mis_profesionales = Profesional.objects.all()

    mis_profesionales = Profesional.objects.raw("select * from appweb_profesional where especialista = true")


    data = {
        'profesionales' : mis_profesionales,
        'saludo' : "Hola Sebastian"
    }

    data["correo"] = "seba@core.cl"

    return render(request, "profesionales.html", data)

def agregar_profesional(request):

    data = {
        "form" : ProfesionalForm
    }
    if request.method == "POST":
        formulario = ProfesionalForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "El profesional se ha guardado"
        else:
            data["mensaje"] = "Hubo un error"
            data["form"] = formulario

    return render(request, "mantenedor/profesional/agregar.html", data)




@login_required(login_url='/accounts/login')
@permission_required(['appweb.view_profesional'], login_url='/accounts/login')
def listar_profesionales(request):

    profes = Profesional.objects.all()

    data = {
        "profesionales" : profes
    }


    return render(request, "mantenedor/profesional/listar.html", data)

def modificar_profesional(request, rut):

    profesional = get_object_or_404(Profesional, rut=rut)

    data = {
        "form": ProfesionalForm(instance=profesional)
    }

    if request.method == 'POST':
        formulario = ProfesionalForm(data=request.POST, files=request.FILES, instance=profesional)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_profesionales")
        else:
            data["mensaje"] = "Hubo un error"
            data["form"] =  formulario


    return render(request, "mantenedor/profesional/modificar.html", data)

def eliminar_profesional(request, rut):
    profesional = get_object_or_404(Profesional, rut=rut)

    profesional.delete()
    messages.success(request, "El profesional rut: "+ rut + " fue eliminado correctamente")
    return redirect(to="listar_profesionales")

def login_usuario(request):
    print("Bienvenido "+ request.user.username)


    print("Grupos", request.user.groups.all())

    if request.user.groups.filter(name='profesional'):
        print("Es un profesional")

    return redirect(to='home')

def registro_profesional(request):
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
            grupo = Group.objects.get(name='profesional')
            try:
                usu.save()
                usu.groups.add(grupo)
                data["mensaje"] = "Usuario creado"
                user = authenticate(username=usu.username, password=password1)
                login(request, user)
                return redirect(to='home')
            except:
                data["mensaje"] = "Error"
    return render(request, "registration/registro.html", data)






def registrar_atencion(request):

    data = {
        "mensaje": ""
    }



    if request.POST:
        monto = request.POST.get("monto")
        observacion = request.POST.get("observacion")
        usu = User.objects.get(username=request.user.username)

 
        #try:
        atencion = Atencion()
        atencion.fecha = datetime.datetime.now()
        atencion.observacion = observacion
        atencion.monto = monto
        atencion.usuario = usu

        atencion.save()

        messages.success(request, "Atencion creada")
        #except:
        data["mensaje"] = "Error"
  


    return render(request, "registrar_atencion.html")