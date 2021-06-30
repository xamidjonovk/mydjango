from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    age = models.IntegerField()



