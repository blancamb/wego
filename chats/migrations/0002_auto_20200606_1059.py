# Generated by Django 3.0.7 on 2020-06-06 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='owner',
            new_name='club',
        ),
    ]
