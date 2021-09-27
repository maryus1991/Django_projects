import os
import random
from django.db import models


def upload_image_file(instance, filename):
    BaseName = os.path.basename(filename)
    if instance.id is None:
        instance.id = random.randint(1, 32165469879)

    count = len(BaseName) + len(instance.title) + len(instance.description)
    name, ext = os.path.splitext(BaseName)
    new_name = random.randint(1000, 10000000000)
    final = instance.id + new_name + count + len(name)
    final_name = f'images/{final}-{instance.title}{ext}'
    return final_name


class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    link = models.URLField(verbose_name="ادرس / لینک")
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_image_file, verbose_name='عکس')
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title
