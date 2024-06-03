from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import os
from datetime import datetime

class CheckFilesView(APIView):
    def post(self, request):
        # Obtener los datos enviados en la solicitud POST
        files = request.data.get('files', [])

        # Inicializar una lista para almacenar los resultados de la verificación
        response = []

        # Iterar sobre cada archivo en la lista recibida
        for file in files:
            # Construir la ruta completa del archivo en la carpeta test_files
            file_path = os.path.join(settings.BASE_DIR, 'test_files', file)
            
            # Verificar si el archivo existe en el sistema de archivos
            if os.path.exists(file_path):
                # Obtener la última fecha de modificación del archivo
                last_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                # Construir un diccionario con el nombre del archivo y la fecha de última modificación
                file_info = {'file': file, 'last_modified': last_modified_time}
                # Agregar el diccionario a la lista de respuesta
                response.append(file_info)
            else:
                # Si el archivo no existe, construir un diccionario con el nombre del archivo y un mensaje de error
                file_info = {'file': file, 'error': 'File does not exist'}
                # Agregar el diccionario a la lista de respuesta
                response.append(file_info)

        # Devolver una respuesta HTTP con la lista de resultados
        return Response(response, status=status.HTTP_200_OK)
 