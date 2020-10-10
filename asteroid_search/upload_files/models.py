from django.db import models

class UploadFiles(models.Model):
    name = models.CharField(max_length=100)
