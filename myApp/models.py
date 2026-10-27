from django.db import models

# Create your models here.

class clothes(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
