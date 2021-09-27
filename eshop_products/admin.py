from django.contrib import admin
from .models import Product
from .models import ProductGallery


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']

    class Meta:
        model = Product


class ProductGalleriesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'product']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery, ProductGalleriesAdmin)
