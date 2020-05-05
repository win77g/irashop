from .models import *
from rest_framework import serializers


class QuethenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuethenModel
        fields = ('id','name','phone','email','message','created','updated')



