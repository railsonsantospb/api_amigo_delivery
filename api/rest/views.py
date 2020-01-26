from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ClientSerializer
from .models import Client
from rest_framework.authentication import TokenAuthentication
# Create your views here.

# ViewSets define the view behavior.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_class = (TokenAuthentication,)
