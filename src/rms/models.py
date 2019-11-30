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

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=30)
    about = models.TextField(null=True)

