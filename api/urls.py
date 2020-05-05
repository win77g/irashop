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
from wishlist.views import WishlistPost,WishlistViewSet,DeleteWishlist
from quethen.views import QuethenViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'postel', ProductViewSet)
router.register(r'product', ProductItemViewSet)
router.register(r'producthome', GetProductForHomeViewSet)
router.register(r'tkan', ProductTcanViewSet)
router.register(r'brend', ProductBrendViewSet)
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
    path('deletewishlist/',DeleteWishlist.as_view()),

]\
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
