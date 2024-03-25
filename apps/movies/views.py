from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Movie
from django.http import JsonResponse
from .serializer import MovieDetailSerializer
from rest_framework.authentication import TokenAuthentication  
from rest_framework.permissions import IsAuthenticated  
from datetime import date

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

    
    authentication_classes = [TokenAuthentication]  # Agrega la autenticación que deseas
    permission_classes = [IsAuthenticated]  # Ajusta los permisos según tus necesidades


    """ Generador de Reportes """
    @action(detail=False, methods=['GET'])
    def generar_reporte(self, request, rating=None):
        try:
            rating = int(rating)

            if rating < 1 or rating > 5:
                return Response({'error': 'El rating debe estar entre 1 y 5.'}, status=status.HTTP_400_BAD_REQUEST)

            movies_query = Movie.objects.filter(rating=rating)

            serialized_data = MovieDetailSerializer(movies_query, many=True).data

            response = JsonResponse(serialized_data, safe=False)

            response['Content-Disposition'] = 'attachment; filename="reporte.json"'

            return response

        except ValueError:
            return Response({'error': 'El rating debe ser un número válido.'}, status=status.HTTP_400_BAD_REQUEST)

   

    """ Metodo para filtrar peliculas mayores al año 2010"""
    @action(detail=False, methods=['GET'])
    def filtrar(self, *args, **kwargs):
        fecha_filtrados = date(2010, 1, 1)
        queryset = Movie.objects.filter(release_date__gte=fecha_filtrados)
        serializer = MovieDetailSerializer(queryset, many = True)
        return Response(serializer.data)

