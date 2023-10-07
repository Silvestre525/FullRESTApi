from django.urls import path
from .views import PersonViewSet

urlpatterns = [
    path("", PersonViewSet.as_view({"get": "list", "post": "create"}), name="Personas-list"),
]
