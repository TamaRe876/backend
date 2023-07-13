from django.db import models



class Person(models.Model):
    fullname = models.CharField(max_length=200)
    phone = models.IntegerField()