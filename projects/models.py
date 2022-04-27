import email
from email import message
from operator import mod
from django.db import models

# Create your models here.
class Project(models.Model):
    name =  models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()


    def __str__(self):
        return self.name