from django.db import models
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()