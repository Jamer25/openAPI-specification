# openAPI-specification

En Django REST Framework (DRF), un serializador es una clase que convierte datos complejos (como modelos de Django) en formatos como JSON, XML, etc., y viceversa. También se encarga de validar los datos entrantes.

# drf-spectacular necesita conocer el serializador de una vista para poder generar correctamente la documentación OpenAPI, ya que el serializador define:

La estructura de los datos que la vista devuelve (respuestas).

La estructura de los datos que la vista recibe (solicitudes).

