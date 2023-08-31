from django.urls import path
from .views import MovieViewSet

urlpatterns = [
    path('movies/', MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie-list'),
    path('movies/<int:pk>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='movie-detail'),
    path('movies/<int:pk>/rate-movie/', MovieViewSet.as_view({'post': 'rate_movie'}), name='rate-movie'),
]
