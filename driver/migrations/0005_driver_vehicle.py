# Generated by Django 3.2.5 on 2021-08-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_driver_driver_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='vehicle',
            field=models.CharField(default='stl', max_length=50),
        ),
    ]