# Generated by Django 2.0.5 on 2018-06-04 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicios', '0012_auto_20180604_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='users',
        ),
        migrations.AddField(
            model_name='service',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]