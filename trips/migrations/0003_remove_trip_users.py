# Generated by Django 3.0.7 on 2020-06-08 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_trip_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='users',
        ),
    ]
