# Generated by Django 3.2.4 on 2021-06-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_alter_request_trip_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='trip_time',
            field=models.CharField(max_length=50),
        ),
    ]
