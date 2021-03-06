# Generated by Django 3.2.5 on 2021-08-11 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maintainance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(max_length=50)),
                ('driver', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('mtype', models.CharField(max_length=50)),
                ('date', models.CharField(blank=True, max_length=50)),
                ('transport', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MajorMaintainance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(max_length=50)),
                ('spare', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending')], default='Pending', max_length=50)),
                ('human', models.CharField(max_length=50)),
            ],
        ),
    ]
