from django.shortcuts import render
from .models import Series
from rest_framework import viewsets
from .serializer import SeriesSerializer

class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

    #Las Acciones Crud Convencionales se generan automaticamente por ModelViewSet

