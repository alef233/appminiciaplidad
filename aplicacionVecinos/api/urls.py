from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PublicacionViewSet,
    UsuarioViewSet,
    CategoriaViewSet,
    JuntaVecinalViewSet,
    EvidenciaViewSet
)

# Crear un enrutador
router = DefaultRouter()

# Registrar los ViewSets
router.register(r'publicaciones', PublicacionViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'evidencias', EvidenciaViewSet)

# Incluir las rutas generadas por el enrutador
urlpatterns = router.urls