from django.urls import path
from .views import MovieViewSet

urlpatterns = [
    path("", MovieViewSet.as_view({"get": "list", "post": "create"}), name="movies-list"),
    path("<int:pk>/", MovieViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="movies-detail"),
    path('buscar/<int:pk>/', MovieViewSet.as_view({'get': 'buscar'}), name='buscar'),
]
