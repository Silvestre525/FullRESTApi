from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.views import SwaggerUIRenderer


# Define el esquema Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Tu API",
        default_version="v1",
        description="Descripción de tu API",
        terms_of_service="https://www.tu-api.com/terms/",
        contact=openapi.Contact(email="contact@tu-api.com"),
        license=openapi.License(name="Tu Licencia"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include("apps.movies.urls")),
    path('series/', include("apps.series.urls")),
    path('person/', include("apps.users.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
