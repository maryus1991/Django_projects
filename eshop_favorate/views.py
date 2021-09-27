from django.shortcuts import render, redirect
from .models import FavorateItemDetail, FavorateItem
from eshop_products.models import Product
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import FavorateItem as FavorateItemForm


@login_required(login_url='/auth/login')
def favorate_page(request):
    favorate = FavorateItem.objects.filter(owner=request.user, active=True).first()
    if favorate is None:
        favorate = FavorateItem.objects.create(owner=request.user)
    favorate_item = FavorateItemDetail.objects.filter(favorateitem=favorate, active=True).all()
    new_order_form = FavorateItemForm(request.POST or None)
    context = {
        'favorate': favorate,
        'favorate_item': favorate_item,
        'new_order_form': new_order_form
    }

    return render(request, 'favorate_page.html', context)


@login_required(login_url='/auth/login')
def remove_favorate_item(request, *args, **kwargs):
    remove_id = kwargs.get('removeid')
    try:
        favorateitemdetail = FavorateItemDetail.objects.get_queryset().get(id=remove_id,
                                                                           favorateitem__owner_id=request.user.id)
        if favorateitemdetail is not None:
            favorateitemdetail.delete()
        else:
            Http404()
    except:
        Http404('')
    return redirect('/favorates/favorate-page')


@login_required(login_url='/auth/login')
def add_favorate_item(request, *args, **kwargs):
    new_order_form = FavorateItemForm(request.POST or None)
    if new_order_form.is_valid():
        productid = new_order_form.cleaned_data.get('pk')
        favorateitem = FavorateItem.objects.filter(owner=request.user, active=True).first()
        if favorateitem is None:
            favorateitem = FavorateItem.objects.create(owner=request.user)

        product = Product.objects.filter(id=productid)
        favorateitem.favorateitemdetail_set.create(product_id=productid)
    return redirect('/favorates/favorate-page')
