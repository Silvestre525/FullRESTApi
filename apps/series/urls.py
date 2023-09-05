from django.urls import path
from .views import SeriesViewSet

urlpatterns = [
    path("", SeriesViewSet.as_view({"get": "list", "post": "create"}), name="movies-list"),
    path("<int:pk>/", SeriesViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="movies-detail"),
]
