# Generated by Django 5.1.4 on 2025-01-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_artwork_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
