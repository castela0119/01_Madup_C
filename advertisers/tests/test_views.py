from django.urls import reverse
from rest_framework import status, test

from ..models import Client


class ClientCreationTest(test.APITestCase):
    '''
    Assignee : 장우경
    Reviewer : 김수빈
    '''
    def setUp(self):
        self.data = {
            'id' : 1,
            'client_number' : 11111111,
            'name' : 'LS',
            'contact_number' : '02-111-1111',
            'email' : 'ls@naver.com'
        }
        self.response = self.client.post(
            reverse('client_creation'),
            self.data,
            format='json')

    def test_post_success_client_creation(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.all().count(), 1)
        self.assertEqual(Client.objects.get(client_number=11111111).name, 'LS')

    def test_get_success_client_list(self):
        url = reverse('client_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Client.objects.count(), 1)

    def test_get_success_client_detail(self):
        client = Client.objects.get()
        response = self.client.get(
            reverse('client_detail', kwargs={'pk': client.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
