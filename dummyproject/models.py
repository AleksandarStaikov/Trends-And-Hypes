from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    cool = models.BooleanField(null=True, blank=True)