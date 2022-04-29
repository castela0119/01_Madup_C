from rest_framework import generics, status
from rest_framework.response import Response

from .models import Client
from .serializers import ClientSerializer


class ClientView(generics.CreateAPIView):
    """
    Assignee : 장우경
    Reviewer : -
    """
    def post(self, request):
        serializer = ClientSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        client, is_created = Client.objects.get_or_create(
            client_number = serializer.data['client_number'],
            defaults = {
                'name': serializer.data['name'],
                'email' : serializer.data['email'],
                'contact_number': serializer.data['contact_number']
            }
        )
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class ClientListView(generics.ListAPIView):
    def get(self, request):
        clients = Client.objects.all()
        serializers = ClientSerializer(clients, many=True)
    
        return Response(serializers.data, status = status.HTTP_200_OK)
