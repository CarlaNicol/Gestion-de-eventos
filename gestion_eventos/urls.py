from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, AsistenteViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'asistentes', AsistenteViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
