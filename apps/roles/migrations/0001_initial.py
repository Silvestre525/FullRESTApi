# Generated by Django 4.0.4 on 2024-01-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=50)),
                ('level_of_access', models.IntegerField(blank=True, db_column='level-access')),
            ],
        ),
    ]
