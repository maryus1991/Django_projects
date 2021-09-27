import itertools
from django.shortcuts import redirect, render
from eshop_sliders.models import Slider
from eshop_settings.models import SiteSetting
from eshop_products.models import Product


def header(request, *args, **kwargs):
    logo = SiteSetting.objects.first()
    return render(request, 'shared/Header.html', {'logo': logo.logo.url})


def footer(request, *args, **kwargs):
    about_us = SiteSetting.objects.first()
    return render(request, 'shared/Footer.html', {'about_us': about_us})


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    sliders = Slider.objects.filter(active=True).all()
    most_visited = Product.objects.order_by('-visit_count').all()[:8]
    lastest_product = Product.objects.order_by('-id').all()[:8]
    # most_selled_product = Product.objects.order_by('-sell_count').all()[:8]
    most_visited = my_grouper(4, most_visited)
    context = {
        'sliders': sliders,
        'most_visited': most_visited,
        'lastest_product': my_grouper(4, lastest_product),
        # 'most_selled_product': my_grouper(4, most_selled_product)

               }
    return render(request, 'index.html', context)


def notfound(request):
    return render(request, '404.html', {})


def about_page(request):
    setting = SiteSetting.objects.first()
    context = {
        'setting': setting
    }
    return render(request, "about_page.html", context)
