from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import *
from quethen.serializers import *
class QuethenViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.IsAuthenticated, ]
    queryset = QuethenModel.objects.all()
    serializer_class = QuethenModelSerializer
