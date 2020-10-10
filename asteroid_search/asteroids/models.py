from django.db import models

class Observatories(models.Model):
    code = models.CharField(max_length=50)

class Devices(models.Model):
    code = models.CharField(max_length=50)
    resolution = models.CharField(max_length=10)
    observatory = models.ForeignKey(Observatories, on_delete=models.CASCADE, default=1)

class AsteroidRegistration(models.Model):
    date = models.DateTimeField()
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    matrix = models.CharField(max_length=200)
