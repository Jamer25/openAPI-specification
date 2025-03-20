# openAPI-specification
 drf-spectacular es una herramienta excelente para generar automáticamente la especificación OpenAPI (en formato YAML o JSON) a partir de tus modelos, vistas y serializadores en Django REST Framework (DRF). No solo documenta tus endpoints, sino que también genera el archivo .yml o .json que describe toda tu API de manera estructurada.
En Django REST Framework (DRF), un serializador es una clase que convierte datos complejos (como modelos de Django) en formatos como JSON, XML, etc., y viceversa. También se encarga de validar los datos entrantes.

Se integra con Django REST Framework :

Funciona directamente con DRF, por lo que no necesitas definir manualmente la especificación OpenAPI. Todo se genera automáticamente.

# drf-spectacular necesita conocer el serializador de una vista para poder generar correctamente la documentación OpenAPI, ya que el serializador define:

La estructura de los datos que la vista devuelve (respuestas).

La estructura de los datos que la vista recibe (solicitudes).

# Comenzando:

## Primero creamos un entorno virtual:
    Un entorno virtual es un espacio en donde las versiones de nuestro programa serán una, y no se mezclarán con otras diferentes, en caso tengamos otro programa que usa distintas versiones

Con el comando:
    python -m virtualenv venv

Para hacer esto tenemos que instalar virtualenv, podemos hacerlo con:
    pip install virtualenv


Ahora vamos activarlo:
    .\venv\Scripts\activate
con gitbash:
    source venv/Scripts/activate


Ahora si instalamos Django:
    pip install django

Ahora iniciamos el proyecto de Django
    django-admin startproject myproject .
El punto es para que se cree una carpeta en el mismo directorio

Ahora creamos una aplicación:
(Recordamos que django la estructura que trabaja es proyecto y luego dentro de ese lo que queramos se llamarán app)

    django-admin startapp myapp

Instalamos también:
    pip install drf-spectacular
Porque:
        drf-spectacular necesita conocer el serializador de una vista para poder generar correctamente la documentación OpenAPI, ya que el serializador define:

        La estructura de los datos que la vista devuelve (respuestas).

        La estructura de los datos que la vista recibe (solicitudes).

Luego con esto ya tenemos nuestra estructura básica
En nuestra carpeta drf que se creó cuando creamos el proyecto en django, en el archivo settings.py agregamos:
    'drf_spectacular'
    'myapp'
En:
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_spectacular',  # Agrega drf_spectacular 
    'myapp',

]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',  # Configura el esquema automático
}

Ahora ya podemos comenzar:

## En views.py de myapp agregamos:

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

@extend_schema(
    responses={
        200: {
            "type": "object",
            "properties": {
                "message": {"type": "string"}
            }
        }
    }
)
@api_view(['GET'])
def example_view(request):
    return Response({"message": "Hello, world!"})

## En urls.py de myapp agregamos:

from django.urls import path
from .views import example_view

urlpatterns = [
    path('example/',example_view, name='example'),
]

## Creamos serializers.py para que pueda conevertir de complejo a json o xml
from rest_framework import serializers

class ExampleSerializer(serializers.Serializer):
    message = serializers.CharField()

## En urls.py de myproject:

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Genera el esquema OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Documentación interactiva de Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    # Incluye las URLs de tu aplicación
    path('api/', include('myapp.urls')),
]


# Ahora generamos el .yml de OpenAPI de lo que hemos creado:
python manage.py spectacular --file api-spec.yml

# Ejecutamos con:
python manage.py runserver