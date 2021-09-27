from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManager


class CategoryManager(TreeManager):
    def all(self):
        return self.get_queryset().filter(active=True)


class ProductCategory(MPTTModel):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    name = models.CharField(max_length=150, verbose_name=' عنوان در URL ')
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال', blank=True)
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children',
                            verbose_name='ارتباط به'
                            )

    objects = CategoryManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def get_absolute_url_categories(self):
        return f'/product/category/{self.name.replace(" ", "-")}'

    class MPTTMeta:
        order_insertion_by = ['title', 'name']
