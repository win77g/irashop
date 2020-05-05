from .models import *
from rest_framework import serializers


class ProductInBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInBasketModel
        fields = ('id','token_key','qty','size','product','price','image',
                  'total_price','is_active','created','updated')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ('id','user','total_price','customer_email','customer_surname','customer_name',
                  'customer_tel','customer_address',
                  'comments','status','created','updated','token')

class ProductInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInOrderModel
        fields = ('id','order','product','nmb','size','price_per_item','image','total_price','is_active','created',
                  'updated')

