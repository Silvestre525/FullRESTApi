from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(models.Model):
    id = models.AutoField(primary_key=True, db_column="users_id")
    name = models.CharField(max_length=20,db_column="name", null=True, blank=True)
    last_name = models.CharField(max_length=30,db_column="last_name",null=True, blank=True)

    class Meta:
        db_table="Users"


    