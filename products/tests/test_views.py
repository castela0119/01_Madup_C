from datetime import date
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.permissions import BasePermission

from products.views import AdsAPIView


# user test를 위한 클래스
class UserTest(BasePermission):
    """
    Assignee : 김수빈
    Reviewer : -
    """
    def get_permission(self, request, view):
        return request.user and request.user.is_superuser


    def get_object_permission(self, request, view, object):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return object == request.user
        else:
            return False


class AdsAPIViewTest(APITestCase):
    def setUp(self):
        pass
