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