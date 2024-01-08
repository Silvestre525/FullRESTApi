from django.db import models

class Roles(models.Model):
    id = models.AutoField(primary_key = True, db_column='id')
    name = models.CharField( max_length=50, db_column='name')
    level_of_access = models.IntegerField( blank=True, db_column='level-access')
    