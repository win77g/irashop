from .models import *
from rest_framework import serializers


class PledSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pled
        fields = ('id','name','brend','tkan','size','type','osobenost','key_words','image','image_link',
                  'slug','price','price_old','description',
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
class OsobenistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osobenost
        fields = ('name','slug')


class PledImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PledImage
        fields = ('id','product','image','slug')
