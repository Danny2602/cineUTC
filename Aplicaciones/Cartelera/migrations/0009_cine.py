# Generated by Django 5.0.6 on 2024-07-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0008_director_fotografia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
    ]
