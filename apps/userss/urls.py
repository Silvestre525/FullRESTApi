from django.urls import path
from .views import PersonViewSet


urlpatterns = [
    path("", PersonViewSet.as_view({"get": "list", "post": "create"}), name="Personas-list"),
    path("<int:pk>/", PersonViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="users-detail"),
]
