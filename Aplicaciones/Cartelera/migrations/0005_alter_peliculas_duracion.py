# Generated by Django 4.0.6 on 2024-06-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0004_peliculas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='duracion',
            field=models.TimeField(),
        ),
    ]
