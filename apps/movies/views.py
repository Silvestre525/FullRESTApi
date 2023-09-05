from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Movie
from .serializer import MovieDetailSerializer # Asegúrate de importar MovieDetailSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

    # Otras acciones CRUD generadas automáticamente por ModelViewSet...

    @action(detail=True, methods=['GET'])
    def buscar(self, request, pk=None):
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieDetailSerializer(movie)  # Usar el serializador personalizado
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response({'error': 'La película no existe.'}, status=status.HTTP_404_NOT_FOUND)
