from .models import *
from rest_framework import serializers


class PokryvalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokryvala
        fields = ('id','name','brend','tkan','size','dekor','key_words','image','image_link',
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

class DekorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dekor
        fields = ('name','slug')



class PokryvalaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokryvalaImage
        fields = ('id','product','image','slug')
