from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import *
from .models import *
# Create your views here.
class BigSliderViewSet(viewsets.ModelViewSet):
      permission_classes = [permissions.AllowAny, ]
      queryset = BigSliderImageModel.objects.all()
      serializer_class = BigSliderImageSerializer

class AdvertisingImageViewSet(viewsets.ModelViewSet):
      permission_classes = [permissions.AllowAny, ]
      queryset = AdvertisingImageModel.objects.all()
      serializer_class = AdvertisingImageModelSerializer
