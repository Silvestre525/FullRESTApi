from django.shortcuts import render
from rest_framework import generics
from .models import Person
from rest_framework import viewsets
from .serializer import PersonSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated


@permission_classes([IsAuthenticated])
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    
    def get_permissions(self):
        if self.action == "destroy":
            permission_classes = [IsAuthenticated]  # Cambiado a IsAuthenticated para requerir autenticación
        elif self.action in ("create", "update", "list"):
            permission_classes = [AllowAny]  # Cambiado a AllowAny para permitir acceso a todas estas acciones
        else:
            permission_classes = []  # Si ninguna acción coincide, se establecen permisos vacíos

        return [permission() for permission in permission_classes]
    