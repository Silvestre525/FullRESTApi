from django.urls import path
from .views import SeriesViewSet

urlpatterns = [
    path("", SeriesViewSet.as_view({"get": "list", "post": "create"}), name="series-list"),
    path("<int:pk>/", SeriesViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="series-detail"),
    path("carga/", SeriesViewSet.as_view({"post": "carga_series"}), name="carga_series"),
]
