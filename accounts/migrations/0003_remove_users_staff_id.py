# Generated by Django 3.2.4 on 2021-06-09 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_users_staff_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='staff_id',
        ),
    ]