from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cargo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
 
class Mecanico(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(null=True, upload_to='mecanicos')
    
 
    def __str__(self):
        return self.rut
    

list_tipo_contacto = [
    [0, "Presupuesto"],
    [1, "Reclamo"]
    
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    tipo_contacto = models.IntegerField(choices=list_tipo_contacto)
    mensaje = models.TextField()


    def __str__(self):
        return self.nombre   
    
list_categoria = [
    [0, "Mantencíon de kilometraje"],
    [1, "Cambio de aceite"],
    [2, "Frenos"],
    [3, "Baterías"],
    [4, "Scanner y diagnostico"],
    [5, "otros"]
    

    
]
class Atencion(models.Model):
    fecha = models.DateField()
    monto = models.IntegerField()
    Modelo = models.CharField(max_length=100)
    categoria = models.IntegerField(choices=list_categoria)
    observacion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fotografia = models.ImageField(null=True, upload_to='categoria')

    def __str__(self):
        return self.observacion
