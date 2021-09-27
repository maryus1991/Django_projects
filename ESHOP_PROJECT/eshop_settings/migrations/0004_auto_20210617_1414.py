# Generated by Django 3.2.3 on 2021-06-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0003_auto_20210525_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='copy_right',
            field=models.CharField(default=1, max_length=200, verbose_name='متن کپی رایت'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='maliat',
            field=models.IntegerField(default=9, verbose_name='درصد مالیات'),
        ),
    ]
