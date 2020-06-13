from .models import *
from rest_framework import serializers


class DetskaPostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetskaPostel
        fields = ('id','name','brend','key_words','image','image_link',
                  'slug','tkan','size','type','price','price_old','description',
                  'description_short','discount','is_active','new_product','top','slider','comments')

class TkanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tkan
        fields = ('name','slug')

class BrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = ('name','slug')
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('name','slug')
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name','slug')
class DetskaPostelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetskaPostelImage
        fields = ('id','product','image','slug')
