from rest_framework import generics, status
from rest_framework.response import Response

from .models import Client
from .serializers import ClientDetailSerializer, ClientSerializer


class ClientView(generics.CreateAPIView):
    '''
    Assignee : 장우경
    Reviewer : 진병수, 김수빈
    '''
    def post(self, request):
        serializer = ClientSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if Client.objects.filter(client_number=serializer.data['client_number']):
            return Response({'message' : 'client_number가 이미 존재합니다.'}, status=status.HTTP_409_CONFLICT)
        
        client = Client.objects.create(
            client_number = serializer.data['client_number'],
            name = serializer.data['name'],
            email = serializer.data['email'],
            contact_number = serializer.data['contact_number']
        )
        
        result = {
            'id' : client.id,
            'client_number' : client.client_number,
            'name' : client.name,
            'email' : client.email,
            'contact_number' : client.contact_number
        }
        
        return Response(result, status=status.HTTP_201_CREATED)


class ClientListView(generics.ListAPIView):
    '''
    Assignee : 장우경
    Reviewer : 진병수
    '''
    def get(self, request):
        clients = Client.objects.all()
        serializers = ClientSerializer(clients, many=True)
    
        return Response(serializers.data, status=status.HTTP_200_OK)


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Assignee : 장우경
    Reviewer : 홍은비
    '''
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
