from django.shortcuts import render
from rest_framework import generics
from .models import Person
from rest_framework import viewsets
from .serializer import PersonSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer