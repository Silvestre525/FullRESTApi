# series/models.py

from django.db import models

class Series(models.Model):
    id = models.AutoField(primary_key=True, db_column="movies_id")
    title = models.CharField(max_length=200, db_column="title")
    director = models.TextField(db_column="director", null=True)
    genero = models.CharField(max_length=100, db_column="genero") 
    rating = models.DecimalField(max_digits=3, decimal_places=1, db_column="rating", null=True)
    premios = models.DecimalField(max_digits=4, decimal_places=1, db_column="premios", null=True)

    class Meta:
        db_table = "Series"
