from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Cargo(models.Model):
    
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
 
class Mecanico(models.Model):
    id_mecanico = models.AutoField(primary_key=True,default=1)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(null=True, upload_to='mecanicos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    ######
 
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
    
class Categoria(models.Model):
    
    nombre_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_categoria    
    
list_categoria = [
    [0, "Mantencíon de kilometraje"],
    [1, "Cambio de aceite"],
    [2, "Frenos"],
    [3, "Baterías"],
    [4, "Scanner y diagnostico"],
    [5, "otros"]
]
class Atencion(models.Model):
    id_atencion = models.AutoField(primary_key=True)

    fecha = models.DateField()
    monto = models.IntegerField()
    Modelo = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacion = models.TextField()
    motivoRechazo = models.TextField(null=True,blank=True)
    Estado = models.CharField(max_length=50, default='Pendiente')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    fotografia = models.ImageField(null=True, upload_to='categoria')

    def __int__(self):
        return self.id_atencion

class Postulante(models.Model):
    id_postulante=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=80)
    email = models.EmailField()
    edad = models.IntegerField()
    cargo_postulacion = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    experiencia = models.CharField(max_length=100)
    fotografia = models.ImageField(null=True, upload_to='postulantes')
    cv= models.FileField(upload_to='cv/')  
 
    def __int__(self):
        return self.id_postulante
    