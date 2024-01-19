# login/views.py
from rest_framework.authtoken.views import ObtainAuthToken
from .serializer import AuthTokenSerializer

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer