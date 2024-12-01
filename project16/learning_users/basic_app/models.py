from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfoModel(models.Model):
    user = models.OneToOneField(User)

    portfolio = models.URLField(max_length=200, blank=True)
    picture = models.ImageField(upload_to="portfolio_pics")

    def __str__(self):
        return self.name