from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Movie
from django.http import JsonResponse
from .serializer import MovieDetailSerializer
from rest_framework.authentication import TokenAuthentication  # Puedes usar la autenticación que desees
from rest_framework.permissions import IsAuthenticated  # Puedes ajustar los permisos según tus necesidades

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

    
    authentication_classes = [TokenAuthentication]  # Agrega la autenticación que deseas
    permission_classes = [IsAuthenticated]  # Ajusta los permisos según tus necesidades


    """ Generador de Reportes """
    @action(detail=False, methods=['GET'])
    def generar_reporte(self, request, rating=None):
        try:
            # Convierte el parámetro 'rating' en un entero.
            rating = int(rating)

            # Verifica si el rating está en el rango válido (1 a 5).
            if rating < 1 or rating > 5:
                return Response({'error': 'El rating debe estar entre 1 y 5.'}, status=status.HTTP_400_BAD_REQUEST)

            # Filtra las películas que tienen el rating deseado.
            movies = Movie.objects.filter(rating=rating)

            # Serializa los resultados a formato JSON.
            serialized_data = MovieDetailSerializer(movies, many=True).data

            # Crear una respuesta JSON.
            response = JsonResponse(serialized_data, safe=False)

            # Configurar encabezados para descarga.
            response['Content-Disposition'] = 'attachment; filename="reporte.json"'

            # Devuelve la respuesta con el archivo JSON descargable.
            return response

        except ValueError:
            return Response({'error': 'El rating debe ser un número válido.'}, status=status.HTTP_400_BAD_REQUEST)

