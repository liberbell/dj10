import os
import django
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

os.environ.setdefault("DJANGO_SETTING_MODULE", "first_project.settings")
django.setup()

fakegen = Faker()
topics = ["Search", "Social", "Marketplace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):

    for entry in range(n):
        top = add_topic()

        fake_url = fakegen.url()
        fale_date = fakegen.date()