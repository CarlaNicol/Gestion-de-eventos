from django.test import TestCase
from .models import Evento
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

class EventoModelTest(TestCase):
    def test_creacion_evento(self):
        evento = Evento.objects.create(
            nombre="Evento de prueba",
            fecha="2024-12-31 23:59",
            lugar="Lugar de prueba",
            descripcion="Descripción de prueba"
        )
        self.assertEqual(evento.nombre, "Evento de prueba")

class EventoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.evento_data = {
            "nombre": "Evento API",
            "fecha": "2024-12-31T23:59:00Z",
            "lugar": "Lugar API",
            "descripcion": "Descripción API"
        }
        self.evento = Evento.objects.create(**self.evento_data)
        self.url = reverse('evento-list')

    def test_get_eventos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_evento(self):
        response = self.client.post(self.url, self.evento_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_evento(self):
        response = self.client.get(reverse('evento-detail', args=[self.evento.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_evento(self):
        updated_data = self.evento_data.copy()
        updated_data['nombre'] = "Evento API Actualizado"
        response = self.client.put(reverse('evento-detail', args=[self.evento.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.evento.refresh_from_db()
        self.assertEqual(self.evento.nombre, updated_data['nombre'])

    def test_delete_evento(self):
        response = self.client.delete(reverse('evento-detail', args=[self.evento.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Evento.objects.filter(id=self.evento.id).exists())

