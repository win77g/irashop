from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from .serializers import *
# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny,]
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer
    filter_fields = ['token_key']
