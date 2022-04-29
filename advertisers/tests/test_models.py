from django.test import TestCase
from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase


from advertisers.models import Client


class ClientModelTest(APITestCase):
    """
    Assignee : 김수빈
    Reviewer : 장우경
    """
    def setUp(self):
        Client.objects.create(
            id = 1,
            client_number = 37443400,
            name = "가가가",
            contact_number = "999-9999-9999",
            email = "aaa@aaa.io",
        )


    def tearDown(self):
        Client.objects.all().delete()

    
    # validation 식은 추후 작성
    def test_validate_data(self):
        pass
