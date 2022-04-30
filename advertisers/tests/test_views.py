from django.urls import reverse
from rest_framework import status, test

from ..models import Client
from ..serializers import ClientSerializer
from ..views import ClientView


class ClientSerializerTest(test.APITestCase):
    """
    Assignee : 김수빈, 장우경
    Reviewer : 장우경, 김수빈
    """
    @classmethod
    def set_up_test_data(self):
        print("APP : advertisers 고정값이 실행됩니다.")
        self.client = Client.objects.create(
            # id = 1,
            client_number = 37443400,
            name = "가가가",
            contact_number = "999-9999-9999",
            email = "aaa@aaa.io",
        )
        self.client.save()
        print("APP : advertisers 고정값이 설정되었습니다.")


    def setUp(self):
        print("APP : advertisers 반복 설정값이 실행됩니다.")
        client_list = [
            Client(
                client_number = 37444234,
                name = "나나나",
                contact_number = "999-9999-9999",
                email = "aaa@aaa.com",
            ),
            Client(
                client_number = 37444673,
                name = "다다다",
                contact_number = "999-9999-9999",
                email = "aaaaa",
            ),
            Client(
                client_number = 37444329,
                name = "라라라",
                contact_number = "999-99999-999",
                email = "aaa@aaa.co.kr",
            ),
            Client(
                client_number = 37443947,
                name = "가가가가",
                contact_number = "99-999-9999",
                email = "aaa@aaaa.tech",
            )
        ]
        Client.objects.bulk_create(client_list)
        print("APP : advertisers 반복 설정값이 설정되었습니다.")


    def test_serialize_success_client(self):
        serializer = ClientSerializer(
            data = {
                'client_number': 37443947,
                'name': "가가가가",
                'contact_number': "999-9999-9999",
                'email': "aaa@aaaa.tech",
            }
        )
        self.assertTrue(serializer.is_valid())
        
    def test_serialize_fail_client(self):
        serializer = ClientSerializer(
            data = {
                self.client
            }
        )
        self.assertTrue(serializer.is_valid(), "SERIALIZE 할 수 없는 데이터가 들어왔습니다.")


class ClientCreationTest(test.APITestCase):
    '''
    Assignee : 장우경, 김수빈
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


class ClientViewTest(test.APITestCase):
    """
    Assignee : 김수빈, 장우경
    Reviewer : 장우경, 김수빈
    """

    def setUp(self):
        client_list = [
            Client(
                client_number = 37444234,
                name = "나나나",
                contact_number = "999-9999-9999",
                email = "aaa@aaa.com",
            ),
            # 이메일 검증할 부분
            Client(
                client_number = 37444673,
                name = "다다다",
                contact_number = "999-9999-9999",
                email = "aaaaa",
            ),
            # 전화번호 검증할 부분
            Client(
                client_number = 37444329,
                name = "라라라",
                contact_number = "999-99999-999",
                email = "aaa@aaa.co.kr",
            ),
            Client(
                client_number = 37443947,
                name = "가가가가",
                contact_number = "99-999-9999",
                email = "aaa@aaaa.tech",
            )
        ]
        Client.objects.bulk_create(client_list)


    def tearDown(self):
        Client.objects.all().delete()


    def test_get_success_client_list(self):
        client = ClientView()
        response = client.get('/api/v1/client/1')
        self.maxDiff = None

        self.assertEqual(
            response.json(),
            {
                'message': 'SUCCESS',
                'data': {
                    'id': 1,
                    'client_number': 37443400,
                    'name': "가가가",
                    'contact_number': "999-9999-9999",
                    'email': "aaa@aaa.io",
                }
            }
        )
        self.assertEqual(response.status_code, 200)
