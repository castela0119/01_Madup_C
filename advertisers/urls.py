from django.urls import path

from .views import ClientDetailView, ClientListView, ClientView


urlpatterns = [
    path('/client', ClientView.as_view()),
    path('/client/list', ClientListView.as_view(), name='client_list'),
    path('/client/<int:pk>', ClientDetailView.as_view()),
]
