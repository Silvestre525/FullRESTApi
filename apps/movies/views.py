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


    """Metodo para cargar peliculas que se encuentran en un Excel"""
    @action(detail=False, methods=['POST'])
    def cargar_movies(self, request):

        try:
            file_1 = request.FILES.get("carga_movies")
            

            if not file_1:
                return Response({"error":"No se encontro ningún archivo"}, status=status.HTTP_400_BAD_REQUEST)

            if not file_1.name.endswith('.xls') and not file_1.name.endswith('.xlsx'):
                return Response({"error": "El archivo no es un archivo Excel válido"}, status=status.HTTP_400_BAD_REQUEST)

            df = pd.read_excel(file_1)
            

            if df.empty:
                return Response({"error": "El archivo está vacío"}, status=status.HTTP_400_BAD_REQUEST)

            movies_created = []
            for index, row in df.iterrows():
                movie_data = {
                    'title': row['title'],
                    'description': row['description'],
                    'genero': row['genero'],
                    'rating': row['rating'],
                    'premios': row['premios'],
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


