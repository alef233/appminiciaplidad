from django.shortcuts import render
from rest_framework import viewsets
from .models import Publicacion, Usuario, Categoria, JuntaVecinal, Evidencia
from .serializers import (
    PublicacionSerializer,
    UsuarioSerializer,
    CategoriaSerializer,
    JuntaVecinalSerializer,
    EvidenciaSerializer
)


# ViewSet para Publicacion
class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer


# ViewSet para Categoria
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# ViewSet para Evidencia
class EvidenciaViewSet(viewsets.ModelViewSet):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerializer
# Create your views here.
