# Generated by Django 5.0.9 on 2024-11-02 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_showroom_name_seat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showroom',
            name='seat_count',
        ),
        migrations.AddField(
            model_name='seat',
            name='row',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
