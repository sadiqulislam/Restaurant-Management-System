from django.db import models
import datetime
# Create your models here.
 #For Chef (List)

class Chef(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    experties = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    bio = models.TextField(null=True)

