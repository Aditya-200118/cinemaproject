# Generated by Django 5.0.9 on 2024-10-29 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_movie_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='screening',
            old_name='showrooms',
            new_name='showroom',
        ),
    ]
