from django.db import models


class SiteSetting(models.Model):
    sitetitle = models.CharField(max_length=150, verbose_name='عنوان سایت')
    address = models.CharField(max_length=500, verbose_name='ادرس')
    telephone = models.CharField(max_length=50, verbose_name='تلفن ثابت')
    mobile = models.CharField(max_length=50, verbose_name='تلفن همراه')
    fax = models.CharField(max_length=50, verbose_name='فکس')
    email = models.CharField(max_length=50, verbose_name='ایمیل سایت')
    about_us = models.TextField(verbose_name='درباره سایت')
    location_img = models.ImageField(upload_to='locations_images/', verbose_name='عکس لوکیشن مورد نظر')
    logo = models.ImageField(upload_to='setting_images/', verbose_name='لوگو سایت')
    is_active = models.BooleanField(default=False, verbose_name='فعال بودن یا نبودن')
    copy_right = models.CharField(max_length=200, verbose_name='متن کپی رایت')
    maliat = models.IntegerField( verbose_name='درصد مالیات' , default=9  )

    class Meta:
        verbose_name = 'تنضیمات سایت'
        verbose_name_plural = 'مدریت تنضیمات'

    def __str__(self):
        return self.sitetitle
