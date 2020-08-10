from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from rest_framework import viewsets,permissions
from order.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# вывод всех продуктов по категории
class ProductInBasketViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.IsAuthenticated, ]
    queryset = ProductInBasketModel.objects.all()
    serializer_class = ProductInBasketSerializer
# AllowAny
class ProductInBasket(APIView):
      permission_classes = [permissions.AllowAny, ]
      def post(self,request):
          print(request.data)
          token_key = request.data.get("token_key")
          qty = request.data.get("qty")
          size = request.data.get("size")
          product = request.data.get("product_name")
          price = request.data.get("price")
          image = request.data.get("image")
          total_price = request.data.get("total_price")
          new_product, created = ProductInBasketModel.objects.get_or_create(token_key=token_key,
                qty=qty,size=size,
                                                                            product=product,
                                                                            price=price,image=image,total_price=total_price)
          if not created:
               new_product.qty += int(qty)
               new_product.total_price += int(total_price)
               new_product.save(force_update=True)
          products_in_basket = ProductInBasketModel.objects.filter(token_key=token_key)

          serializer = ProductInBasketSerializer(products_in_basket,many=True)
          return Response({'data':serializer.data})

class DeleteProductInBasket(APIView):

       def post(self,request):
          id = request.data.get("id")
          token_key = request.data.get("token")
          products_in_basket = ProductInBasketModel.objects.filter(token_key=token_key,id=id)
          products_in_basket.delete()
          products_in_baskets = ProductInBasketModel.objects.filter(token_key=token_key)
          serializer = ProductInBasketSerializer(products_in_baskets,many=True)
          return Response({'data':serializer.data})

class UpdateProductInBasket(APIView):

       def post(self,request):
           data = request.data
           print(data)
           products_in_basket = ProductInBasketModel.objects.filter(id=data["id"])
           for ob in products_in_basket:
             ob.qty = int(data["qty"])
             ob.total_price = data["qty"]*ob.price
             ob.save()
           # serializer = ProductInBasketSerializer(products_in_basket,many=True)
           return Response(status=201)


class Order(APIView):
       def post(self,request):
           data = request.data
           customer_email = data["email"],
        #    print(customer_email)
           products_in_basket = ProductInBasketModel.objects.filter(token_key=data["token_key"], is_active=True)#.exclude(order__isnull=False)
           prod = products_in_basket.values()
           p = list(prod)
           a = []
           for item in p:
              q = int(float(item["total_price"]))
              a.append(q)
              total = sum(a)
           delivery = data["address"]
           user = User.objects.get(auth_token = data["token_key"])
           order = OrderModel.objects.create(user = user,
                                         customer_email = data["email"],
                                         customer_name = data["firstname"],
                                         customer_surname = data["lastname"],
                                         customer_tel = data["phone"],
                                         customer_address = data["address"],
                                         comments = data["comment"],
                                         status_id = 1,
                                         token = data["token_key"])
                                       
           for name in products_in_basket:
                
                if name:
                    id = name.id
                    product_in_baskets = ProductInBasketModel.objects.get(token_key=data["token_key"], is_active=True,id = id )
                    # print(product_in_baskets)
                    product_in_baskets.save(force_update=True)
                    q = ProductInOrderModel.objects.create(
                                                 # id = order.id,
                                                 product = product_in_baskets.product,
                                                 nmb = product_in_baskets.qty,
                                                 size = product_in_baskets.size,
                                                 price_per_item = product_in_baskets.price,
                                                 image = product_in_baskets.image,
                                                 total_price = product_in_baskets.total_price,
                                                 order = order,
                    )
           
           
           html_message = render_to_string('mail_template.html', {'context':prod,'order':order, 'total_price':total, 'delivery':delivery})
           plain_message = strip_tags(html_message)

           send_mail('Percale - Интернет магазин домашнего текстиля',
                              plain_message,
                              'sergsergio777@gmail.com',
                              customer_email, html_message=html_message,
                              )
           products_in_basket.delete()
           return Response(status=201)


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.IsAuthenticated, ]
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
    filter_fields = ('token',)

class ProductInOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.IsAuthenticated, ]
    queryset = ProductInOrderModel.objects.all()
    serializer_class = ProductInOrderSerializer
    filter_fields = ('order',)
