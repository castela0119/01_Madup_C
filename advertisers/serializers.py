from rest_framework import serializers

from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_number', 'name', 'contact_number', 'email']
