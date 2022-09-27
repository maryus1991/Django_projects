from django.db import models


class SiteSetting(models.Model):
    sitetitle = models.CharField(max_length=150, verbose_name='عنوان سایت', default='eshop')
    address = models.CharField(max_length=500, verbose_name='ادرس', default='تهران')
    telephone = models.CharField(max_length=50, verbose_name='تلفن ثابت', default='000000000')
    mobile = models.CharField(max_length=50, verbose_name='تلفن همراه', default='0000000000')
    fax = models.CharField(max_length=50, verbose_name='فکس', default='00000000000')
    email = models.CharField(max_length=50, verbose_name='ایمیل سایت', default='aaa@aaa.aaa')
    about_us = models.TextField(null=True, blank=True, verbose_name='درباره سایت', default=' ')
    location_img = models.ImageField(upload_to='locations_images/', verbose_name='عکس لوکیشن مورد نظر', default='images/home/Map.jpg')
    logo = models.ImageField(upload_to='setting_images/', verbose_name='لوگو سایت', default='images/home/logo.png')
    is_active = models.BooleanField(default=True, verbose_name='فعال بودن یا نبودن')
    copy_right = models.CharField(max_length=200, verbose_name='متن کپی رایت', default=' هرگونه استفاده به جز اهداف سایت به دون اطلاع غیرمجاز می باشد')
    maliat = models.IntegerField( verbose_name='درصد مالیات' , default=9  )

    class Meta:
        verbose_name = 'تنضیمات سایت'
        verbose_name_plural = 'مدریت تنضیمات'

    def __str__(self):
        return self.sitetitle
