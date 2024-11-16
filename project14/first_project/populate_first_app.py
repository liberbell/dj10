import os
import django
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

os.environ.setdefault("DJANGO_SETTING_MODULE", "first_project.settings")
django.setup()

fakegen = Faker()
topics = ["Search", "Social", "Marketplace"]