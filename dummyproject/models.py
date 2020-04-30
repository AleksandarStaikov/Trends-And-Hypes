from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    cool = models.BooleanField(null=True, blank=True)
    date_of_coolness = models.DateTimeField(null=True, blank=True)
    amount_of_coolness = models.DecimalField(decimal_places=2,max_digits=5,null=True, blank=True)
    