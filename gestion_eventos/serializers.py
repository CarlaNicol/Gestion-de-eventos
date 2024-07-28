from rest_framework import serializers
from .models import Evento, Asistente, Comentario

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class AsistenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistente
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
