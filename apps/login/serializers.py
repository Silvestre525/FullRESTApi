# login/serializers.py
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Aquí puedes personalizar los datos que deseas incluir en el token JWT
    # Puedes agregar más campos según tus modelos y requerimientos
    # Ejemplo:
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Aquí puedes añadir campos adicionales al token si es necesario
        # Ejemplo: token["access_level"] = user.role.level_of_access
        return token
