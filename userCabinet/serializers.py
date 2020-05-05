from .models import *
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    token_key = serializers.ReadOnlyField()
    class Meta:
        model = ClientModel
        fields = ('id','lastname','email','firstname','phone','address',
                  'created','updated',
                  'token_key',)
        read_only_fields = ['token_key']
        def update(self, instance, validated_data):
        # Update the Foo instance
             instance.title = validated_data['lastname','email','firstname','phone','address']
             instance.save()
             return instance

