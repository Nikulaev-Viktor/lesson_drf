# Generated by Django 5.1.2 on 2024-11-14 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0006_car_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='amount',
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='moto',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
