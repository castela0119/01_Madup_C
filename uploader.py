import os
import csv
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings") 
django.setup()

from advertisers.models import Client
from products.models import Ads


CSV_PATH = './Madup_Wanted_Data_set.csv'

def insert_client():
    """
    Assignee : 전병수
    Reviewer : 장우경, 홍은비
    """
    with open(CSV_PATH, newline='') as csvfile:
        rows = csv.DictReader(csvfile)

        client_list = []
        
        unq = set(list(map(lambda x: x.get('advertiser'), rows)))
        for row in unq:
            client_list.append(Client(
                client_number = row
            ))

        Client.objects.bulk_create(client_list)
        
        print('CLIENT DATA UPLOADED SUCCESSFULY!')


def insert_ads():
    """
    Assignee : 진병수
    Reviewer : 장우경, 홍은비
    """
    with open(CSV_PATH, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        ads_list = []

        for row in rows:
            date = row['date']
            
            ads_list.append(
                Ads(
                    client = Client.objects.get(client_number=row['advertiser']),
                    platform = row['media'],
                    date = date.replace('.', '-'),
                    cost = row['cost'],
                    impression = row['impression'],
                    click = row['click'],
                    conversion = row['conversion'],
                    cv = row['cv'],
                )
            )
        print(len(ads_list))            
        Ads.objects.bulk_create(ads_list)
        print('ADs DATA UPLOADED SUCCESSFULY!')


# insert_client()
# insert_ads()