from django.db import models

# Create your models here.
class Urls(models.Model):
    inputlink = models.CharField(max_length=20000)
    myid = models.CharField(max_length=10)