# Generated by Django 3.2.2 on 2021-07-13 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0003_alter_interview_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtubevideo',
            name='thumbnail',
        ),
    ]
