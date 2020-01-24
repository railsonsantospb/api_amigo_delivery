from rest_framework import routers, serializers, viewsets
from .models import Cliente
# Serializers define the API representation.
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'cpf', 'nome', 'endereco', 'idade']