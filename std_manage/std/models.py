from django.db import models

# Create your models here.

class User(models.Model):
    uid =  models.IntegerField(max_length = 10)
    uname = models.CharField(max_length=100)
    uemail = models.CharField(max_length=100)
    ucontact = models.CharField(max_length=100)
    
    class Meta:
       db_table = "user"

class persons(models.Model):
    pid =  models.CharField(max_length = 20)
    pname = models.CharField(max_length=100)
    pemail = models.CharField(max_length=100)
    pcontact = models.CharField(max_length=100)
    
    class Meta:
        db_table = "persons"