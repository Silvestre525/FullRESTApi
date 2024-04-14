from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Series
from rest_framework import viewsets, status
from .serializer import SeriesSerializer
from rest_framework.authentication import TokenAuthentication  
from rest_framework.permissions import IsAuthenticated  
import pandas as pd

class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

    #Las Acciones Crud Convencionales se generan automaticamente por ModelViewSet

    authentication_classes = [TokenAuthentication]  # Agrega la autenticación que deseas
    permission_classes = [IsAuthenticated]  # Ajusta los permisos según tus necesidades
    


    """"Carga de series medinte archivo excel"""
    @action(detail = False, method = ['POST'])
    def carga_series(self,request):

        try:
            file_1 = request.FILES.get('carga_series')

            if not file_1:
                return Response({"error ":"No se encontro ningun archivo"}, status=status.HTTP_400_BAD_REQUEST)

            if not file_1.name.endswith('.xls') and not file_1.name.endswith('.xlsx'):
                return Response({"error": "El archivo no se encuentra en un formato valido Excel válido"}, status=status.HTTP_400_BAD_REQUEST)
            
            df = pd.read_excel(file_1)

            if df.empty:
                return Response({"error": "El archivo está vacío"}, status=status.HTTP_400_BAD_REQUEST)


            series_created = []
            for index, row in df.iterrows():
                series_data =  {
                    'title': row['title'],
                    'genero': row['genero'],
                    'rating': row['rating'],
                    'premios': row['premios'],
                    'director': row['director'],
                }

                serializer = SeriesSerializer(data=series_data)
                if serializer.is_valid():    
                    series_instance = serializer.save()
                    series_created.append(series_instance)
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
