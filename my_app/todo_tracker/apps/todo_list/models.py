from django.db import models

class Task(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=50)

