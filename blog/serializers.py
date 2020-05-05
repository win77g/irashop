from .models import *
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','name','category','image','slug','key_word','key_description',
                   'description','description_short','is_active','top','created','updated')

class TegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teg
        fields = ('name','slug')

