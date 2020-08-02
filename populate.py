import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'My_First_App.settings')

import django
django.setup()

## Fake pop script

import random
from first_app.models import  Topic, WebPage

from faker import Faker

fakegen=Faker()

topics=['Search','Social', 'MarketPlace', 'recent photos']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]

    t.save()
    return t

def populate(N):
    for entry in range(N):
        top=add_topic()

        fake_url=fakegen.url()
        fake_date= fakegen.date()
        fake_name=fakegen.company()

        webpg= WebPage.objects.get_or_create(topic=top,url= fake_url,name=fake_name)[0]
if __name__=='__main__':
    print("Populating script")
    populate(20)
    print("Populating completed")