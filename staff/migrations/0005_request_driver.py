# Generated by Django 3.2.4 on 2021-06-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_alter_request_trip_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='driver',
            field=models.CharField(blank=True, default='Not Assigned', max_length=50),
        ),
    ]
