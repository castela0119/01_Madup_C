import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from advertisers.views import (
    ClientView,
    ClientListView, 
    ClientDetailView,
)


class ClientViewTest:
    def setUp(self):
        pass
    
    # def test_get_success_client_detail(self):
    #     client = Client()
    #     response = client.get('/api/v1/client/1')
    #     self.maxDiff = None

    #     self.assertEqual(
    #         response.json(),
    #         {
    #             'message': 'SUCCESS',
    #             'data': {
    #                 'id': 1,
    #                 'client_number': 37443400,
    #                 'name': "가가가",
    #                 'contact_number': "999-9999-9999",
    #                 'email': "aaa@aaa.io",
    #             }
    #         }
    #     )
    #     self.assertEqual(response.status_code, 200)


    # def test_get_fail_client_detail(self):
    #     client = Client()
    #     response = client.get('/api/v1/client/2')
    #     self.maxDiff = None

    #     self.assertEqual(
    #         response.json(),
    #         {'message': 'NO_CLIENT_FOUND'}
    #     )
    #     self.assertEqual(response.status_code, 404)

    # def test_valid_client(self):
    #     client = self.client
    #
    #     self.assertTure(len(client.contact_number.split('-'))==3, "핸드폰 번호의 양식이 맞지 않습니다.")
            


    # def test_create_bulk(self):
    #     client_list = [
    #         Client(
    #             id = 2,
    #             client_number = 37444234,
    #             name = "나나나",
    #             contact_number = "999-9999-9999",
    #             email = "aaa@aaa.com",
    #         ),
    #         # 이메일 검증할 부분
    #         Client(
    #             id = 3,
    #             client_number = 37444673,
    #             name = "다다다",
    #             contact_number = "999-9999-9999",
    #             email = "aaaaa",
    #         ),
    #         # 전화번호 검증할 부분
    #         Client(
    #             id = 4,
    #             client_number = 37444329,
    #             name = "라라라",
    #             contact_number = "999-99999-999",
    #             email = "aaa@aaa.co.kr",
    #         ),
    #         Client(
    #             id = 5,
    #             client_number = 37443947,
    #             name = "가가가가",
    #             contact_number = "99-999-9999",
    #             email = "aaa@aaaa.tech",
    #         )
    #     ]
    #     Client.objects.bulk_create(client_list)

    # def get_contact_number(self):
    #     contact_number = self.client.get(con)
    #     self.assertEqual()


    # def get_fail_case(self):
    #     self.assertEqual(response.status_code, 404)
