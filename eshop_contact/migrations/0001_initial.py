# Generated by Django 3.1.5 on 2021-05-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=100, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=200, verbose_name='موضوع')),
                ('text', models.TextField(verbose_name='متن')),
                ('is_read', models.BooleanField(verbose_name='خوانده شده / نشده')),
            ],
        ),
    ]
