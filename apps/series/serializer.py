from rest_framework import serializers
from .models import Series
from django.core.validators import MaxLengthValidator


class SeriesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=50,
        validators=[MaxLengthValidator(limit_value=50, message='El título no debe superar los 50 caracteres.')]
    )
    class Meta:
        model = Series
        fields = ("__all__")
        