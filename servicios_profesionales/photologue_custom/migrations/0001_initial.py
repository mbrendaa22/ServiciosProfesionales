# Generated by Django 2.0.5 on 2018-06-11 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryExtended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extended', to='photologue.Gallery')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Extra fields',
                'verbose_name_plural': 'Extra fields',
            },
        ),
    ]
