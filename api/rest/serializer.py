from rest_framework import serializers
from .models import Client

# Serializers define the API representation.
class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['cpf', 'nome']