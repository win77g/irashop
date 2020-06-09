from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from .serializers import *
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from .pagination import PostPageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# вывод всех продуктов по категории
class PolotencaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny, ]
    queryset = Polotenca.objects.all()
    serializer_class = PolotencaSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filter_fields = ['slug','brend','consist','size','type','filler_weight','top']

    pagination_class = PostPageNumberPagination#PageNumberPagination #LimitOffsetPagination



class SearchAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    search_fields = ['brend__name','tkan__name','name']
    filter_backends = (SearchFilter,)
    queryset = Polotenca.objects.all()
    serializer_class = PolotencaSerializer

class PolotencaTcanViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Tkan.objects.all()
    serializer_class = TkanSerializer
    # filter_fields = ('slug',)

class PolotencaBrendViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer

class PolotencaSizeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class PolotencaTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Type.objects.all()
    serializer_class = SizeSerializer

class PolotencaFillerWeightViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = FillerWeight.objects.all()
    serializer_class = SizeSerializer

class GetPolotencaImageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = PolotencaImage.objects.all()
    serializer_class = PolotencaImageSerializer
    filter_fields = ('product',)
