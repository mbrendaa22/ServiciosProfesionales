# Generated by Django 2.0.5 on 2018-06-01 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_myuser_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='services',
        ),
    ]
