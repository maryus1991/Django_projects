from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import Product


class FavorateItem(models.Model):
    owner = models.ForeignKey(User, verbose_name="کاربر", on_delete=models.CASCADE)
    active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name = "محصول مورد علاقه"
        verbose_name_plural = "محصولات مورد علاقه"

    def __str__(self):
        return self.owner.username


class FavorateItemDetail (models.Model):
    favorateitem = models.ForeignKey(FavorateItem, verbose_name="سبد محصولات مورد علاقه کاربر ", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="محصول", on_delete=models.CASCADE)
    active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')
    
    class Meta:
        verbose_name = "  جزییات محصول موردعلاقه"
        verbose_name_plural = "جزییات محصولات مورد علاقه"

    def __str__(self):
        return self.product.title
