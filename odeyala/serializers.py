from .models import *
from rest_framework import serializers


class OdeyalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odeyala
        fields = ('id','name','brend','tkan','size','type','filler','filler_weight','key_words','image','image_link',
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
class FillerWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = FillerWeight
        fields = ('name','slug')

class OdeyalaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OdeyalaImage
        fields = ('id','product','image','slug')
