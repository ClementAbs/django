from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    age = models.CharField(max_length=32)
    myinput = models.CharField(max_length=128)
