import os
import django
import random

os.environ["DJANGO_SETTINGS_MODULE"] = "ProTwo.settings"

from faker import Faker
django.setup()
from AppTwo.models import User