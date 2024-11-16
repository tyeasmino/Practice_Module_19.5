# Generated by Django 5.1.2 on 2024-11-01 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=100)),
                ('album_release_date', models.DateField(auto_now=True)),
                ('album_rating', models.CharField(choices=[('1', 'Rating 1'), ('2', 'Rating 2'), ('3', 'Rating 3'), ('4', 'Rating 4'), ('5', 'Rating 5')], max_length=1)),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musiciansmodel')),
            ],
        ),
    ]