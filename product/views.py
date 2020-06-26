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
# вывод всех продуктов по категории
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filter_fields = ['slug','categ','brend','tkan','price_polutorca']

    pagination_class = PostPageNumberPagination#PageNumberPagination #LimitOffsetPagination


# class Search(APIView):
#      permission_classes = [permissions.AllowAny, ]
#      def get(self, request, format):
#         queryset = Product.objects.all()
#         serializer = ProductSerializer
#         filter_backends = [SearchFilter]
#         search_fields = ['categ','brend','tkan']
#         return Response(serializer.data)
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
