# Generated by Django 3.2.2 on 2021-06-21 22:20

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_alter_album_options'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='album',
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
