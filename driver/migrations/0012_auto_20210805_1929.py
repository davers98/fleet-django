# Generated by Django 3.2.5 on 2021-08-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0011_alter_driver_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintainance',
            name='status',
        ),
        migrations.AddField(
            model_name='maintainance',
            name='type',
            field=models.CharField(choices=[('Planned', 'Planned'), ('Non-Planned', 'Nonplanned')], default='Planned', max_length=50),
        ),
        migrations.AlterField(
            model_name='maintainance',
            name='transport',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
