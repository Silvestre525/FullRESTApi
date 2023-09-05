from rest_framework import serializers
from apps.movies.models import Movie

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_date')
