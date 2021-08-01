from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from index.views import index
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
# sitemap urls
from .sitemap import ArticleSitemap,StaticSitemap,DetskaPostelSitemap,OdeyalaSitemap,PledSitemap,PodushkiSitemap,PokryvalaSitemap,PolotencaSitemap,ProductSitemap
# from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap ,index



sitemaps = {
    'static':StaticSitemap,
    'blog': ArticleSitemap,
    'detskoe-postelnoe':DetskaPostelSitemap,
    'odeyala':OdeyalaSitemap,
    'pled':PledSitemap,
    'podushki':PodushkiSitemap,
    'pokryvala':PokryvalaSitemap,
    'polotenca':PolotencaSitemap,
    'postelnoe-belie':ProductSitemap
}

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/', include('api.urls')),
    #path('sitemap.xml',sitemap,{'sitemaps': sitemaps}, name='sitemap'),
    path('sitemap.xml', index, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.index'),
    path('sitemap-<section>.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]\
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

