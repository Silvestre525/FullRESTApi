from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Movie
from django.http import JsonResponse
from .serializer import MovieDetailSerializer
from rest_framework.authentication import TokenAuthentication  
from rest_framework.permissions import IsAuthenticated  
from datetime import date
import pandas as pd
from drf_yasg.utils import swagger_auto_schema

"""Generador para paginar movies de la bd"""
def movie_generator(queryset, page_size):
    for i in range(0,queryset.count(), page_size):
        yield queryset[i:i + page_size]



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

    
    authentication_classes = [TokenAuthentication]  # Agrega la autenticación que deseas
    permission_classes = [IsAuthenticated]  # Ajusta los permisos según tus necesidades

    @swagger_auto_schema(method="GET", query_serializer=MovieDetailSerializer)
    @action(detail=False, methods=['GET'])
    def list(self, reequest, *args, **kwargs):
        page_size = 100
        queryset = self.get_queryset()
        generator = movie_generator(queryset, page_size)

        data = []
        try:
            # Obtener solo una página de datos en cada iteración
            page = next(generator)
            serializer = self.get_serializer(page, many=True)
            data.extend(serializer.data)
        except StopIteration:
            pass  # El generador se detiene cuando no hay más datos
        

        return Response(data)

    """ Generador de Reportes """
    @swagger_auto_schema(method="GET", query_serializer=MovieDetailSerializer)
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
    @swagger_auto_schema(method="GET", query_serializer=MovieDetailSerializer)
    @action(detail=False, methods=['GET'])
    def filtrar(self, *args, **kwargs):
        queryset = Movie.objects.filter(premios__gte=3)
        serializer = MovieDetailSerializer(queryset, many = True)
        return Response(serializer.data)


    """Metodo para cargar peliculas que se encuentran en un Excel"""
    @swagger_auto_schema(method="POST", query_serializer=MovieDetailSerializer)
    @action(detail=False, methods=['POST'])
    def cargar_movies(self, request):

        try:
            file_1 = request.FILES.get("carga_movies")
            

            if not file_1:
                return Response({"error":"No se encontro ningún archivo"}, status=status.HTTP_400_BAD_REQUEST)

            if not file_1.name.endswith('.xls') and not file_1.name.endswith('.xlsx'):
                return Response({"error": "El archivo no se encuentra en un formato valido Excel válido"}, status=status.HTTP_400_BAD_REQUEST)

            df = pd.read_excel(file_1)
            

            if df.empty:
                return Response({"error": "El archivo está vacío"}, status=status.HTTP_400_BAD_REQUEST)

            movies_created = []
            for index, row in df.iterrows():
                movie_data = {
                    'title': row['title'],
                    'genero': row['genero'],
                    'rating': row['rating'],
                    'premios': row['premios'],
                    'director': row['director'],
                }

                serializer = MovieDetailSerializer(data=movie_data)
                if serializer.is_valid():    
                    movie_instance = serializer.save()
                    movies_created.append(movie_instance)
                else:
                   errors = {
                    "message": "Los datos no son validos",
                    "serilizers.errors": serializer.errors
                   }

                   return Response(errors, status=status.HTTP_400_BAD_REQUEST)
                    
                       
                
            
            return Response({"message":"Operacion exitosa"})
        
        except pd.errors.EmptyDataError:
            return Response({"error": "El archivo está vacío"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'error': 'Ocurrió un error inesperado'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


