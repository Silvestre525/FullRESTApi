# Generated by Django 4.0.4 on 2024-04-14 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(db_column='movies_id', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='title', max_length=200)),
                ('director', models.TextField(db_column='director', null=True)),
                ('genero', models.CharField(db_column='genero', max_length=100)),
                ('rating', models.DecimalField(db_column='rating', decimal_places=1, max_digits=3, null=True)),
                ('premios', models.DecimalField(db_column='premios', decimal_places=1, max_digits=4, null=True)),
            ],
            options={
                'db_table': 'Series',
            },
        ),
    ]
