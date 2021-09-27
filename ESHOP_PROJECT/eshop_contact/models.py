from django.db import models


class ContactUs(models.Model):
    fullname = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    text = models.TextField(verbose_name='متن')
    is_read = models.BooleanField(verbose_name='خوانده شده / نشده', default=False)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس های کاربران'

    def __str__(self):
        return self.fullname


