import json
from datetime import date
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.views import AdsAPIView


class AdsAPIViewTest(APITestCase):
    def setUp(self):
        pass