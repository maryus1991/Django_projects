# Generated by Django 3.2.3 on 2021-07-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_comments', '0005_comments_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='edited',
            field=models.BooleanField(default=False, verbose_name='ویرایش شده یا نشده'),
        ),
    ]