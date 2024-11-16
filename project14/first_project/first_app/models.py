from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=254, unique=True)