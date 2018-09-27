from django.db import models


# Create your models here.
class Image(models.Model):
    """
    Image class creating table for Image
    """
    Name = models.CharField(max_length=20)
    Deascription = models.CharField(max_length=40)
