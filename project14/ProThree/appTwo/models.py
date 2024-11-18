from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=1024)