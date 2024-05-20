from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=512, default="END.")
    borrowed = models.IntegerField(default = 0)
    returnID = models.CharField(max_length=128, default="") #added for FLAW 2, but I will keep it here
    returnTime = models.IntegerField(default=0) #added for FLAW 3: returnTime, but I will keep it here

class Log(models.Model): #added for FLAW 4, but kept for peer-review simplicity
    timestamp = models.IntegerField(default=0)
    request = models.CharField(max_length=100)
    available = models.IntegerField(default=0)
    status = models.CharField(max_length=20)
