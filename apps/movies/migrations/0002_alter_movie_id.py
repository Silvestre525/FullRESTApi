# Generated by Django 4.0.4 on 2023-09-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.AutoField(db_column='movies_id', primary_key=True, serialize=False),
        ),
    ]
