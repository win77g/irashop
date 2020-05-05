from .models import *
from rest_framework import serializers


class WishlistModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistModel
        fields = ('id','token_key','product_name'
                  ,'slug','price_1','price_2','price_3','price_4'
                  ,'image',
                  'tkan','brend',
                  'created')


