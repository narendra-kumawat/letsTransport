# Generated by Django 3.2.15 on 2022-12-19 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rideinfo',
            old_name='date',
            new_name='datetime',
        ),
    ]
