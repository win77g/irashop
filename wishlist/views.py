from django.shortcuts import render
from .models import *
from product.models import Product
from rest_framework import viewsets,permissions
from wishlist.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from detskoePostelnoe.models import DetskaPostel
from pled.models import Pled
from podushki.models import Podushki
from odeyala.models import Odeyala
from polotenca.models import Polotenca
from pokryvala.models import Pokryvala
# Create your views here.

class WishlistViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = WishlistModel.objects.all()
    serializer_class = WishlistModelSerializer


def querySet_to_list(qs):
    """
    this will return python list<dict>
    """
    return [dict(q) for q in qs]

class WishlistPost(APIView):
       def post(self,request):
           pr = []
           print(request.data)
           slug = request.data.get("product_name")
           token_key = request.data.get("token_key")
           category = request.data.get("category")
           if (category == 'detskoe-postelnoe'):
            pr = DetskaPostel.objects.filter(slug=slug).values()
           if (category=='pled'):
            pr = Pled.objects.filter(slug=slug).values()
           if (category=='postelnoe-belie'):
            pr = Product.objects.filter(slug=slug).values()
           if (category=='podushki'):
            pr = Podushki.objects.filter(slug=slug).values()
           if (category=='odeyala'):
            pr = Odeyala.objects.filter(slug=slug).values()
           if (category=='polotenca'):
            pr = Polotenca.objects.filter(slug=slug).values()
           if (category=='pokryvala'):
            pr = Pokryvala.objects.filter(slug=slug).values()
           product = querySet_to_list(pr)
           print(pr)
           product = product[0]
           print(product)
           wish = WishlistModel.objects.get_or_create(token_key = token_key,
                                         product_name = product["name"],
                                         slug = slug,
                                         price_1 =  product["price_polutorca"],
                                         price_2 =  product["price_dvuspal"],
                                         price_3 =  product["price_semeuka"],
                                         price_4 =  product['price_euro'],
                                         image = product["image"],
                                         tkan = product["tkan_id"],
                                         brend = product["brend_id"])

           return Response({'status':201})

class WishlistPostDp(APIView):
       def post(self,request):
           pr = []
           print(request.data)
           slug = request.data.get("product_name")
           token_key = request.data.get("token_key")
           category = request.data.get("category")
           if (category == 'detskoe-postelnoe'):
            pr = DetskaPostel.objects.filter(slug=slug).values()
           if (category=='pled'):
            pr = Pled.objects.filter(slug=slug).values()
           if (category=='postelnoe-belie'):
            pr = Product.objects.filter(slug=slug).values()
           if (category=='podushki'):
            pr = Podushki.objects.filter(slug=slug).values()
           if (category=='odeyala'):
            pr = Odeyala.objects.filter(slug=slug).values()
           if (category=='polotenca'):
            pr = Polotenca.objects.filter(slug=slug).values()
           if (category=='pokryvala'):
            pr = Pokryvala.objects.filter(slug=slug).values()

           product = querySet_to_list(pr)
           print(pr)
           product = product[0]
           print(product)
           wish = WishlistDpModel.objects.get_or_create(token_key = token_key,
                                         product_name = product["name"],
                                         slug = slug,
                                         price =  product["price"],
                                         image = product["image"],
                                         tkan = product["tkan_id"],
                                         brend = product["brend_id"])

           return Response({'status':201})

class DeleteWishlist(APIView):

       def post(self,request):
          print(request.data)
          slug = request.data.get("slug")
          token_key = request.data.get("token_key")
          wishlist = WishlistModel.objects.filter(token_key=token_key,slug=slug)
          wishlist.delete()
          wishlist = WishlistModel.objects.filter(token_key=token_key)
          serializer = WishlistModelSerializer(wishlist,many=True)
          return Response({'data':serializer.data})
