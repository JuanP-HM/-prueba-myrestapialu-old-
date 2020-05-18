from .models import Alumno, Materia, Grupo
from rest_framework import serializers

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = ('url','nombre','no_control','carrera','foto')
        
class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materia
        fields = ('url','nombre','clave','no_semestre')
        
class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grupo
        fields = ('url','clave','alumnos','materia')