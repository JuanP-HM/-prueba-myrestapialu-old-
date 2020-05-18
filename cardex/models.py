from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=32)
    no_control = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)
    carrera = models.CharField(max_length=32)
    foto = models.ImageField(upload_to="fotos-alumnos")
    
class Materia(models.Model):
    nombre = models.CharField(max_length=32)
    clave = models.CharField(max_length=6)
    no_semestre = models.IntegerField()
    
class Grupo(models.Model):
    clave = models.CharField(max_length=6)
    alumnos = models.ManyToManyField(Alumno, blank=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

# Create your models here.
