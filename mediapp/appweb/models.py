from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cargo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Profesional(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    especialista = models.BooleanField()
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(null=True, upload_to='profesionales')
 
    def __str__(self):
        return self.rut
    
list_tipo_contacto = [
    [0, "Sugerencia"],
    [1, "Reclamo"],
    [2, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    tipo_contacto = models.IntegerField(choices=list_tipo_contacto)
    mensaje = models.TextField()


    def __str__(self):
        return self.nombre
    
class Atencion(models.Model):
    fecha = models.DateField()
    monto = models.IntegerField()
    observacion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.observacion

    


