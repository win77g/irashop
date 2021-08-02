from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.urls import reverse
from blog.models import Blog
from detskoePostelnoe.models import DetskaPostel 
from odeyala.models import Odeyala
from pled.models import Pled
from podushki.models import Podushki
from pokryvala.models import Pokryvala
from polotenca.models import Polotenca
from product.models import Product
# class Site:
#     domain = '127.0.0.1:8000/#/blog/'

class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'
    # def get_urls(self, site=None, **kwargs):
    #     site = Site()
    #     return super(ArticleSitemap, self).get_urls(site=site, **kwargs)
 
    def items(self):
        return Blog.objects.all()
    
    def location(self, obj):
        return '/blog/%s '% obj.slug
 
    def lastmod(self, obj):
        return obj.modified_date 

class DetskaPostelSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'
    # def get_urls(self, site=None, **kwargs):
    #     site = Site()
    #     return super(ArticleSitemap, self).get_urls(site=site, **kwargs)
 
    def items(self):
        return DetskaPostel.objects.all()
    
    def location(self, obj):
        return '/#/product/detskoe-postelnoe/%s '% obj.slug
 
    def lastmod(self, obj):
        return obj.updated        
class OdeyalaSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'
   
    def items(self):
        return Odeyala.objects.all()
    
    def location(self, obj):
        return '/#/product/odeyala/%s '% obj.slug
 
    def lastmod(self, obj):
        return obj.updated     

class PledSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'
   
    def items(self):
        return Pled.objects.all()
    
    def location(self, obj):
        return '/#/product/pled/%s '% obj.slug
 
    def lastmod(self, obj):
        return obj.updated 

class PodushkiSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'
   
    def items(self):
        return Podushki.objects.all()
    
    def location(self, obj):
        return '/#/product/podushki/%s '% obj.slug
 
    def lastmod(self, obj):
        return obj.updated         

class PokryvalaSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'
   
    def items(self):
        return Pokryvala.objects.all()
    
    def location(self, obj):
        return '/#/product/pokryvala/%s '% obj.slug
 
    def lastmod(self, obj):
        return obj.updated      

class PolotencaSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'
   
    def items(self):
        return Polotenca.objects.all()
    
    def location(self, obj):
        return '/#/product/polotenca/%s '% obj.slug
 
    def lastmod(self, obj):
        return obj.updated     

class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'
   
    def items(self):
        return Product.objects.all()
    
    def location(self, obj):
        return '/#/product/postelnoe-belie/%s '% obj.slug
 
    def lastmod(self, obj):
        return obj.updated   

class StaticViewSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['contact','delivery','pay']

    def location(self, item):
        return '/#/%s '%item     