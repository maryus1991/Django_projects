from django.db import models
from eshop_products.models import Product

# Create your models here


class VisitCount(models.Model):
    ip = models.CharField(max_length=20, verbose_name='ای پی')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')
    username = models.CharField(null=True, blank=True, max_length=150, verbose_name='نام کاربری')
    products = models.ManyToManyField(Product, verbose_name='محصولات')
    user_id = models.IntegerField(verbose_name='ایدی کاربر', null=True, blank=True)

    def __str__(self):
        if self.username is not None:
            return self.username
        else:
            return self.ip

    class Meta:
        verbose_name = 'بازید'
        verbose_name_plural = 'بازدید کندگان'
