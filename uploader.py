import os
import csv
import django

from advertisers.models import Client
from products.models import Ads


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings") 
django.setup()

CSV_PATH = './Madup_Wanted_Data_set.csv'


def insert_client():
    """
    Assignee : 전병수
    Reviewer : 장우경, 홍은비
    """
    with open(CSV_PATH, newline='') as csvfile:
        rows = csv.DictReader(csvfile)

        for row in rows:
            Client.objects.create(
                client_number = row['advertiser'],
            )
        print('CLIENT DATA UPLOADED SUCCESSFULY!')


def insert_ads():
    """
    Assignee : 진병수
    Reviewer : 장우경, 홍은비
    """
    with open(CSV_PATH, newline='') as csvfile:
        rows = csv.DictReader(csvfile)        
        id = 0    
        for row in rows: 
            # print(row)

            date = row['date']
            date = date.replace('.', '-')

            id += 1

            client = Client.objects.filter(id=id).values()

            Ads.objects.create (
                client_id = client[0]['id'],
                platform = row['media'],
                date = date,
                cost = row['cost'],
                impression = row['impression'],
                click = row['click'],
                conversion = row['conversion'],
                cv = row['cv'],
            )
        print('ADs DATA UPLOADED SUCCESSFULY!')

insert_client()
insert_ads()