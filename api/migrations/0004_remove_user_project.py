# Generated by Django 4.1.7 on 2023-05-19 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='project',
        ),
    ]
