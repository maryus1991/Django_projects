from django.db import models
from eshop_products.models import Product
from django.db.models.signals import pre_save
from .utils import unique_slug_generator


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='عنوان در url')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    active = models.BooleanField(default=True, verbose_name='فعال | غیر فعال')
    products = models.ManyToManyField(Product, blank=True, verbose_name='محصولات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def get_absolutely_url(self):
        return '/tag/' + str(self.slug)


def tag_pre_save_receiver(sender, instance, *arg, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    return instance.slug


pre_save.connect(tag_pre_save_receiver, sender=Tag)
