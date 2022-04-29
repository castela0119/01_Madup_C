from django.urls import path
from .views import AdsAPIView
urlpatterns = [
    path('/ads', AdsAPIView.as_view(), name='ads'),
]
