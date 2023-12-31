from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=512, default="END.")
    borrowed = models.IntegerField(default = 0)
    returnID = models.CharField(max_length=30, default="") #added for F1.2, but I will keep it here
    returnTime = models.IntegerField(default=0) #added for F2, but I will keep it here

class Log(models.Model): #added for F4, but kept
    timestamp = models.IntegerField(default=0)
    request = models.CharField(max_length=100)
    borrowed = models.IntegerField(default=0)
    tokens = models.IntegerField(default=0)
