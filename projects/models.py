import email
from email import message
from operator import mod
from pyexpat import model
from django.db import models
from datetime import datetime
# Create your models here.
class Project(models.Model):
    name =  models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    submited_on = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name



class Deadline(models.Model):
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.date)