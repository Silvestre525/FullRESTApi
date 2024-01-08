from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import Person


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):

        #esto es lo que estoy obteniendo por body desde el postman
        credentials = {
            'username': attrs.get('username'),
            'password': attrs.get('password'),
        }

        if all(credentials.values()):
            ##Aca se obtiene la info que hay en la base de datos desde mi modelo de users
            user = Person.objects.filter(username=credentials['username']).first()

            #aca se hace la comparacion de lo que obtube en mi base de datos con lo que estoy pasadno por body desde el postman 
            if user and user.check_password(credentials['password']) and user.is_active:
                refresh = RefreshToken.for_user(user)
                data = {}
                data['refresh'] = str(refresh)
                data['access'] = str(refresh.access_token)

                return data

        raise serializers.ValidationError(
            detail="No hay usuarios activos",
            code='authentication_failed'
        )
