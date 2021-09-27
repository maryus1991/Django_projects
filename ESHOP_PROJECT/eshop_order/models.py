from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='پرداخت شده یا نشده')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name=' تاریخ پرداخت ')
    total_price = models.IntegerField(null=True, blank=True)
    refid = models.CharField(max_length=50, null=True, blank=True, verbose_name='کد پیگیری')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید کاربران'

    def __str__(self):
        full_name = self.owner.get_full_name()

        if full_name != '':
            result = full_name
        else:
            result = self.owner.get_username()
        return result

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت')
    count = models.IntegerField(verbose_name='تعداد')

    def get_detail_sum(self):
        return self.count * self.price

    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'اطلاعات جزییات محولات'

    def __str__(self):
        return self.product.title


class Coppone_Model(models.Model):
    title = models.CharField(max_length=50, verbose_name= ' نام به لاتینی باشد' )
    max_used = models.IntegerField(verbose_name='تعداد')
    current_used = models.IntegerField(verbose_name='تعداد استفاده شده ', null=True, blank=True, default = 0 )
    percent = models.IntegerField(verbose_name= 'درصد تخفیف', default=9)
    can_used = models.IntegerField(verbose_name='توان استفاده هر شخص از این کد')
    active = models.BooleanField(default = True, verbose_name= ' فعال / غیر فعال')
    # todo : add witch product

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد های تخفیف'

    def __str__(self):
        return self.title
