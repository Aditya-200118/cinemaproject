# Generated by Django 5.0.9 on 2024-11-01 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_ticket_ticket_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking.tickettype'),
        ),
    ]