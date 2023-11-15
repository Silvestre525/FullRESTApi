# series/models.py

from django.db import models

class Series(models.Model):
    id = models.AutoField(primary_key=True, db_column="series_id")
    title = models.CharField(max_length=200, db_column="title")
    release_date = models.DateField(db_column="release_date")
    creator = models.CharField(max_length=100,db_column="creator")
    description = models.TextField(db_column="description")

    class Meta:
        db_table = "Series"
