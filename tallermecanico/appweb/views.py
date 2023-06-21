from django.shortcuts import render ,redirect,get_object_or_404

# Create your views here.
def principal(request):
    return render(request, "principal.html")

def contacto(request):
    return render(request, "contacto.html")

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

def loginusuario(request):
    return render(request, "loginusuario.html")

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
    return render(request, "pagmecanicos.html")

def perfilMecCamila(request):
    return render(request, "perfilMecCamila.html")

def perfilmecJuan(request):
    return render(request, "perfilmecJuan.html")

def perfilMecMario(request):
    return render(request, "perfilMecMario.html")

def perfilMecPamela(request):
    return render(request, "perfilMecPamela.html")

def perfilMecPedro(request):
    return render(request, "perfilMecPedro.html")

def perfilmecSofia(request):
    return render(request, "perfilmecSofia.html")

def tareasadministrador(request):
    return render(request, "tareasadministrador.html")

def adminAtencion(request):
    return render(request, "adminAtencion.html")

def adminMecanico(request):
    return render(request, "adminMecanico.html")

def formularioRegistroAtencion(request):
    return render(request, "formularioRegistroAtencion.html")
