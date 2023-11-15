# movies/models.py

from django.db import models

class Movie(models.Model):
    id = models.AutoField(primary_key=True, db_column="movies_id")
    title = models.CharField(max_length=200, db_column="title")
    release_date = models.DateField(db_column="release_date")
    director = models.CharField(max_length=100, db_column="director")
    description = models.TextField(db_column="description")
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True,db_column="rating")

    class Meta:
        db_table = "Movies"
