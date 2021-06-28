from django.db import models

# Create your models here.
class Administrater(models.Model):
    username  = models.CharField(max_length=500)
    password  = models.CharField(max_length=500)