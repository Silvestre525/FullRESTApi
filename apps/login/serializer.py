# login/serializer.py
from rest_framework import serializers
from django.contrib.auth import  authenticate

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            raise serializers.ValidationError('no se pudo autenticar', code='authorization')

        data['user'] = user
        return data
