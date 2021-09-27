from django.db import models
# from mptt.models import MPTTModel
from eshop_products.models import Product
from django.contrib.auth.models import User


class Comments(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    full_date = models.DateTimeField(verbose_name='تاریخ و وقت', auto_now_add=True)
    text = models.TextField(verbose_name='متن')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    email = models.CharField(max_length=150, verbose_name='ایمیل')
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    edited_date = models.DateTimeField(verbose_name='تاریخ و وقت ویرایش شده', null=True, blank=True, auto_now=True)
    edited = models.BooleanField(verbose_name='ویرایش شده یا نشده', default=False)
    owner = models.ForeignKey(User, verbose_name='کاربر', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.full_name

