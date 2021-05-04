from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=20)


