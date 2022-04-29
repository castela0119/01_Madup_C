from datetime import date

from django.test import TestCase
from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase

from advertisers.models import Client
from products.models import Ads


class AdsModelTest(APITestCase):
    """
    Assignee : 김수빈
    Reviewer : 장우경
    """
    def setUp(self):
        client = Client.objects.create(
            id = 1,
            client_number = 37444234,
            name = "가가가",
            contact_number = "999-9999-9999",
            email = "aaa@aaa.io",
        )
        Ads.objects.create(
            client = client,
            platform = 'naver',
            date = date.today(),
            cost = 20000,
            impression = 210,
            click = 54,
            conversion = 8,
            cv = 462800,
        )


    def tearDown(self):
        Client.objects.all().delete()
        Ads.objects.all().delete()

    
    # validation 식은 추후 작성
    def test_validate_data(self):
        pass
