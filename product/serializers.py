from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','brend','categ','key_words','image','image_link',
                  'slug','tkan','price_polutorca','price_old_polutorca',
                  'price_dvuspal','price_old_dvuspal','price_semeuka','price_old_semeuka',
                  'price_euro','price_old_euro','description','size_map','description_short',
                  'discount','is_active','new_product','top','slider','comments')

class TkanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tkan
        fields = ('name','slug')
class BrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = ('name','slug')
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id','product','image','slug')
