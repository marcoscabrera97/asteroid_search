# Generated by Django 3.1.2 on 2020-10-10 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asteroids', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsteroidRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('matrix', models.IntegerField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asteroids.devices')),
                ('observatory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asteroids.observatories')),
            ],
        ),
    ]
