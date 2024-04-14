from rest_framework import serializers
from apps.movies.models import Movie
from django.core.validators import MaxLengthValidator


class MovieDetailSerializer(serializers.ModelSerializer):

    # Agrega una validación personalizada al campo 'title'
    title = serializers.CharField(
        max_length=50,
        validators=[MaxLengthValidator(limit_value=50, message='El título no debe superar los 50 caracteres.')]
    ) 

    class Meta:
        model = Movie
        fields = ("__all__")
