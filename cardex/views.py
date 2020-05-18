from django.shortcuts import render

from .models import Alumno, Materia, Grupo
from rest_framework import viewsets
from cardex.serializers import AlumnoSerializer, MateriaSerializer, GrupoSerializer

# Create your views here.
class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allowe materias to be viewed or edited.
    """
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows grupos to be viewed or edited.
    """
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer