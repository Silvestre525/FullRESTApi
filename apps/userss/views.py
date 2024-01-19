from rest_framework import viewsets
from .models import User
from .serializer import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PersonSerializer

