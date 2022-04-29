from django.urls import path

from .views import ClientListView, ClientView

urlpatterns = [
    path('/client', ClientView.as_view()),
    path('/client/list', ClientListView.as_view()),
]
