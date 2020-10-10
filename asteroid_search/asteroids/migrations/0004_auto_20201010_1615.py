# Generated by Django 3.1.2 on 2020-10-10 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asteroids', '0003_auto_20201010_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asteroidregistration',
            name='matrix',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='devices',
            name='observatory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='asteroids.observatories'),
        ),
    ]