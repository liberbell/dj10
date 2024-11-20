import os
os.environ.setdefault("DJANGO_SETTIMGS_MODULE", "ProThree.settings")

import django
django.setup()

from appTwo.models import User
from faker import Faker

