# Generated by Django 3.2.5 on 2021-08-06 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0016_maintainance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='refilling',
            name='approved',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
