from .models import *
from rest_framework import serializers


class PodushkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podushki
        fields = ('id','name','brend','tkan','size','type','filler','key_words','image','image_link',
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

class FillerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filler
        fields = ('name','slug')


class PodushkiImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodushkiImage
        fields = ('id','product','image','slug')
