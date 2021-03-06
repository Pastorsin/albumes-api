# Generated by Django 3.2.2 on 2021-07-14 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0004_remove_youtubevideo_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='interview',
            unique_together={('name', 'youtube_video')},
        ),
    ]
