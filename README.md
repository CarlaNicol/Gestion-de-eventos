# Proyecto de Gestión de Eventos

Este proyecto es una aplicación Django para la gestión de eventos. Permite crear, listar, actualizar y eliminar eventos.

## Requisitos

- Python 3.x
- Django 5.0.7
- Django REST Framework

## Instalación

1. Clonar el repositorio:
    ```
    git clone https://github.com/CarlaNicol/Gestion-de-eventos.git
    cd eventos
    ```

2. Crear un entorno virtual e instalar las dependencias:
    ```
    python -m venv env
    # En Windows: env\Scripts\activate
    pip install -r requirements.txt
    ```

3. Configurar la base de datos:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Crear un superusuario:
    ```
    python manage.py createsuperuser
    ```

5. Ejecutar el servidor de desarrollo:
    ```
    python manage.py runserver
    ```

## Pruebas
python manage.py createsuperuser
user
correo
password

http://127.0.0.1:8000/admin/gestion_eventos/evento/add/

http://127.0.0.1:8000/api/eventos/
http://127.0.0.1:8000/api/asistentes/
http://127.0.0.1:8000/api/comentarios/
http://127.0.0.1:8000/admin/gestion_eventos/comentario/
