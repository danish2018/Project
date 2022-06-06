from django.db import models

# Create your models here.


class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Contact(models.Model):
    Name = models.CharField(max_length= 100)
    Email =models.CharField(max_length= 100)
    Tell_us = models.TextField()
