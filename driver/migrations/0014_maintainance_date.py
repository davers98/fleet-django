# Generated by Django 3.2.5 on 2021-08-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0013_rename_type_maintainance_mtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintainance',
            name='date',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]