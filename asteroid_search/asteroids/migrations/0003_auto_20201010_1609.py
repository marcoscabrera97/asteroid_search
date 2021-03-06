# Generated by Django 3.1.2 on 2020-10-10 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asteroids', '0002_asteroidregistration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asteroidregistration',
            name='observatory',
        ),
        migrations.AddField(
            model_name='devices',
            name='observatory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='asteroids.observatories'),
            preserve_default=False,
        ),
    ]
