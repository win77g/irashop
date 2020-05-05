from .models import *
from rest_framework import serializers


class BigSliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigSliderImageModel
        fields = ('category','lozung','brendi','image','slug','is_active')

class AdvertisingImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingImageModel
        fields = ('image','text','text2','link','is_active')


#
# class ProductInOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductInOrderModel
#         fields = ('id','order','product','nmb','size','price_per_item','image','total_price','is_active','created',
#                   'updated')

