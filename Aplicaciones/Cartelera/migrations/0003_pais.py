# Generated by Django 4.0.6 on 2024-05-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0002_director_genero_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('continente', models.CharField(max_length=50)),
                ('capital', models.CharField(max_length=50)),
            ],
        ),
    ]
