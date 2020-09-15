from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Diseases(models.Model):
    title=models.CharField(max_length=100)
    symptoms=models.ArrayField(models.CharField(max_length=200),blank=True)
