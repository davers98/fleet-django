# Generated by Django 3.2.5 on 2021-08-16 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0031_alter_driver_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='added_by',
            field=models.CharField(max_length=50),
        ),
    ]