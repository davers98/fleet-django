# Generated by Django 3.2.5 on 2021-08-15 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_request_approved_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='trip_status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]