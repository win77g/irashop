from rest_framework import routers
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from product.views import GetProductForHomeViewSet,GetProductImageViewSet,SearchAPIView,ProductViewSet,ProductItemViewSet,ProductTcanViewSet,ProductBrendViewSet
from order.views import ProductInBasketViewSet,Order,OrderViewSet,ProductInOrderViewSet
from order.views import ProductInBasket,DeleteProductInBasket,UpdateProductInBasket
from blog.views import BlogViewSet,TegViewSet
from users.views import UserViewSet
from userCabinet.views import ClientViewSet
from home.views import BigSliderViewSet,AdvertisingImageViewSet
from wishlist.views import WishlistPost,WishlistViewSet,DeleteWishlist,WishlistPostDp
from quethen.views import QuethenViewSet
from detskoePostelnoe.views import DetskaPostelTypeViewSet,DetskaPostelSizeViewSet,DetskaPostelViewSet,DetskaPostelTcanViewSet,DetskaPostelBrendViewSet
from odeyala.views import OdeyalaViewSet,OdeyalaTcanViewSet,OdeyalaBrendViewSet,OdeyalaSizeViewSet,OdeyalaTypeViewSet,OdeyalaFillerViewSet,OdeyalaFillerWeightViewSet
from polotenca.views import PolotencaViewSet,PolotencaTcanViewSet,PolotencaBrendViewSet,PolotencaSizeViewSet,PolotencaTypeViewSet,PolotencaFillerWeightViewSet
from podushki.views import PodushkiViewSet,PodushkiTcanViewSet,PodushkiBrendViewSet,PodushkiSizeViewSet,PodushkiTypeViewSet,PodushkiFillerViewSet
from pled.views import PledViewSet,PledTcanViewSet,PledBrendViewSet,PledSizeViewSet,PledTypeViewSet,PledOsobenostViewSet
from pokryvala.views import PokryvalaViewSet,PokryvalaTcanViewSet,PokryvalaBrendViewSet,PokryvalaSizeViewSet,PokryvalaDekorViewSet
from users.views import SendMailForNewEmail,PasswordResetView
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

router.register(r'product', ProductItemViewSet)
router.register(r'producthome', GetProductForHomeViewSet)
#постельное бельё
router.register(r'postelnoe-belie', ProductViewSet)
router.register(r'postelnoe-belie-tkan', ProductTcanViewSet)
router.register(r'postelnoe-belie-brend', ProductBrendViewSet)
# Детское постельное
router.register(r'detskoe-postelnoe', DetskaPostelViewSet)
router.register(r'detskoe-postelnoe-tkan', DetskaPostelTcanViewSet)
router.register(r'detskoe-postelnoe-brend', DetskaPostelBrendViewSet)
router.register(r'detskoe-postelnoe-size', DetskaPostelSizeViewSet)
router.register(r'detskoe-postelnoe-type', DetskaPostelTypeViewSet)
# Одеяла
router.register(r'odeyala',       OdeyalaViewSet)
router.register(r'odeyala-tkan',  OdeyalaTcanViewSet)
router.register(r'odeyala-brend', OdeyalaBrendViewSet)
router.register(r'odeyala-size',  OdeyalaSizeViewSet)
router.register(r'odeyala-type',  OdeyalaTypeViewSet)
router.register(r'odeyala-filler',  OdeyalaFillerViewSet)
router.register(r'odeyala-fillerweight',  OdeyalaFillerWeightViewSet)
# Плед
router.register(r'pled',       PledViewSet)
router.register(r'pled-tkan',  PledTcanViewSet)
router.register(r'pled-brend', PledBrendViewSet)
router.register(r'pled-size',  PledSizeViewSet)
router.register(r'pled-type',  PledTypeViewSet)
router.register(r'pled-osobenost',  PledOsobenostViewSet)
# Подушки
router.register(r'podushki',       PodushkiViewSet)
router.register(r'podushki-tkan',  PodushkiTcanViewSet)
router.register(r'podushki-brend', PodushkiBrendViewSet)
router.register(r'podushki-size',  PodushkiSizeViewSet)
router.register(r'podushki-type',  PodushkiTypeViewSet)
router.register(r'podushki-filler',  PodushkiFillerViewSet)
# Покрывала
router.register(r'pokryvala',       PokryvalaViewSet)
router.register(r'pokryvala-tkan',  PokryvalaTcanViewSet)
router.register(r'pokryvala-brend', PokryvalaBrendViewSet)
router.register(r'pokryvala-size',  PokryvalaSizeViewSet)
router.register(r'pokryvala-dekor', PokryvalaDekorViewSet)
# Плед
router.register(r'polotenca',            PolotencaViewSet)
router.register(r'polotenca-tkan',       PolotencaTcanViewSet)
router.register(r'polotenca-brend',      PolotencaBrendViewSet)
router.register(r'polotenca-size',       PolotencaSizeViewSet)
router.register(r'polotenca-type',       PolotencaTypeViewSet)
router.register(r'polotenca-fillerweight',  PolotencaFillerWeightViewSet)

router.register(r'productinorder', ProductInBasketViewSet)
router.register(r'getuser',ClientViewSet),
router.register(r'getorder',OrderViewSet),
router.register(r'productinorderbyid',ProductInOrderViewSet),
router.register(r'gallery',GetProductImageViewSet),
router.register(r'bigslider',BigSliderViewSet)
router.register(r'advetising',AdvertisingImageViewSet)
router.register(r'blog',BlogViewSet)
router.register(r'teg',TegViewSet)
router.register(r'wishlist',WishlistViewSet)

router.register(r'quethen',QuethenViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('search/', SearchAPIView.as_view()),
    path('productinbasket/', ProductInBasket.as_view()),
    path('deleteproductinbasket/', DeleteProductInBasket.as_view()),
    path('updateproductinbasket/', UpdateProductInBasket.as_view()),
    path('order/',Order.as_view()),
    path('wishlispost/',WishlistPost.as_view()),
    path('wishlistdp/',WishlistPostDp.as_view()),
    path('deletewishlist/',DeleteWishlist.as_view()),
    path('changepassword/',SendMailForNewEmail.as_view()),
    path('password/reset/confirm/', PasswordResetView.as_view(),),
]\
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
