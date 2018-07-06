# Generated by Django 2.0.5 on 2018-06-11 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        ('servicios', '0015_remove_service_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='gallery',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='photologue.Gallery'),
            preserve_default=False,
        ),
    ]