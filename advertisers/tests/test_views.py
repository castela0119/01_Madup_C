from django.urls import reverse
from rest_framework import status, test


class ClientTest(test.APITestCase):
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
        self.response = self.client.get(
            reverse('client_list'),
            self.data,
            format='json')

    def test_get_success_client_list(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
