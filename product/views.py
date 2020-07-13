from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from product.serializers import *
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from .pagination import PostPageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters import rest_framework as filters

# вывод всех продуктов по категории
class ProductFilter(filters.FilterSet):
    polutorca = filters.NumberFilter(field_name="price_polutorca", lookup_expr='gte')
    dvuspal = filters.NumberFilter(field_name="price_dvuspal", lookup_expr='gte')
    semeuka = filters.NumberFilter(field_name="price_semeuka", lookup_expr='gte')
    euro = filters.NumberFilter(field_name="price_euro", lookup_expr='gte')
    class Meta:
        model = Product
        fields = ['polutorca','dvuspal','semeuka','euro','slug','categ','brend','tkan',]
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    # filter_fields = ['slug','categ','brend','tkan','price_polutorca',]
    filterset_class = ProductFilter
    pagination_class = PostPageNumberPagination#PageNumberPagination #LimitOffsetPagination



class SearchAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    search_fields = ['categ__name','brend__name','tkan__name','name']
    filter_backends = (SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('slug',)

class ProductTcanViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Tkan.objects.all()
    serializer_class = TkanSerializer
    # filter_fields = ('slug',)

class ProductBrendViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer

class GetProductImageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    filter_fields = ('product',)

class GetProductForHomeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('tkan','new_product','top')
