from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    
