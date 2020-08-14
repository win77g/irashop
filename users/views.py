from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets,permissions
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

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

class SendMailForNewEmail(APIView):
    permission_classes = [permissions.AllowAny, ]
    def post(self,request):
        data = request.data
        customer_email = data["email"]
           
        print(customer_email)
        html_message = render_to_string('change_password_template.html')
        plain_message = strip_tags(html_message)

        send_mail('Percale - Интернет магазин домашнего текстиля',
                              plain_message,
                              'sergsergio777@gmail.com',
                              [customer_email,], html_message=html_message,)
        return Response(status=201)  

class PasswordResetView(APIView):
    def get (self, request, uid, token):
        post_data = {'uid': uid, 'token': token}
        print(post_data)
        return Response(post_data)       