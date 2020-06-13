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
class PokryvalaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny, ]
    queryset = Pokryvala.objects.all()
    serializer_class = PokryvalaSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filter_fields = ['slug','brend','tkan','size','dekor']
    pagination_class = PostPageNumberPagination#PageNumberPagination #LimitOffsetPagination



class SearchAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    search_fields = ['brend__name','tkan__name','name']
    filter_backends = (SearchFilter,)
    queryset = Pokryvala.objects.all()
    serializer_class = PokryvalaSerializer

class PokryvalaTcanViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Tkan.objects.all()
    serializer_class = TkanSerializer

class PokryvalaBrendViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer

class PokryvalaSizeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class PokryvalaDekorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Dekor.objects.all()
    serializer_class = DekorSerializer

class GetPokryvalaImageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = PokryvalaImage.objects.all()
    serializer_class = PokryvalaImageSerializer
    filter_fields = ('product',)

