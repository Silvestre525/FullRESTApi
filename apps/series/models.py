# series/models.py

from django.db import models

class Series(models.Model):
    id = models.AutoField(primary_key=True, db_column="series_id")
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    creator = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
