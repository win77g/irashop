from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets,permissions
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny, ]
    queryset = User.objects.all().order_by('-date_joined')
    # queryset = User.objects.filter(email = 'win21g@mail.ru')
    serializer_class = UserSerializer
    filter_fields = ('email','username')

class GetUser(APIView):
    permission_classes = [permissions.AllowAny, ]
    def get(self,request):
      token = request.data.get("token")
      user = Token.objects.get(key=token).user
      serializer = UserSerializer(user)
      return Response({'data':serializer.data})
