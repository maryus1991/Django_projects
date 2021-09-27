from django.db.models import Q 
from django.db import models 
import os
import random
from eshop_products_category.models import ProductCategory

# Create your models here.


def upload_image_file(instance, filename):
    BaseName = os.path.basename(filename)
    if instance.id is None:
        instance.id = random.randint(1, 32165469879)
    count = len(BaseName) + len(instance.title) + len(instance.description) + instance.price
    name, ext = os.path.splitext(BaseName)
    new_name = random.randint(1000, 10000000000)
    final = instance.id + new_name + instance.price + count + len(name)
    final_name = f'images/{final}-{len(instance.title)}{ext}'
    return final_name


class ProductManager(models.Manager):
    def get_active_product(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(category__name__iexact=category_name, active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (Q(description__icontains=query) |
                  Q(title__icontains=query) |
                  Q(tag__title__icontains=query)

                  )
        return Product.objects.filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_file, null=True, blank=True, default='images/product.jpg', verbose_name='عکس')
    active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    category = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی ها')
    new = models.BooleanField(default=True, verbose_name='محصول جدید')
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    sell_count = models.IntegerField(verbose_name='میزان فروش', default=0)
    about_maker = models.TextField(verbose_name='درباره سازنده')

    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = ' محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/product/{self.id}/{self.title.replace(" ","-")}'


def upload_gallery_images_file(instance, filename):
    BaseName = os.path.basename(filename)
    if instance.id is None:
        instance.id = random.randint(1, 32165469879)

    count = len(BaseName) + len(instance.title)
    name, ext = os.path.splitext(BaseName)
    new_name = random.randint(1000, 10000000000)
    final = instance.id + new_name + count + len(name)
    final_name = f'images/{final}-{instance.title}{ext}'
    return final_name


class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_gallery_images_file)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'


    def __str__(self):
        return self.title





