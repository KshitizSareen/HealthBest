from django.db import models

# Create your models here.
class Diseases(models.Model):
    title=models.CharField(max_length=100)
    symptoms=models.TextField(default="")
