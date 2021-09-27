from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from eshop_products.models import Product
from .forms import UserNewOrder, Coppone
from .models import Order, Coppone_Model, OrderDetail
from eshop_settings.models import SiteSetting
from eshop_favorate.forms import FavorateItem
# from zeep import Client
import datetime
import random


@login_required(login_url='/auth/login')
def add_user_order(request):
    new_order_form = UserNewOrder(request.POST or None, initial={'count': 1})
    print(new_order_form.is_valid())
    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        productid = new_order_form.cleaned_data.get('productid')
        count = new_order_form.cleaned_data.get('count')

        product = Product.objects.filter(id=productid).first()
        product.sell_count += 1
        product.save()

        if count <= 0:
            count = 1
        product = Product.objects.get_by_id(product_id=productid)
        order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
        return redirect(f'/product/{product.id}/{product.title.replace(" ", "-")}')

    FavorateItemForm = FavorateItem(request.POST or None)
    if FavorateItemForm.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        productid = FavorateItemForm.cleaned_data.get('pk')
        product = Product.objects.filter(id=productid).first()
        product.sell_count += 1
        product.save()

        product = Product.objects.get_by_id(product_id=productid)
        order.orderdetail_set.create(product_id=product.id, price=product.price, count=1)
        return redirect('/order/user_open_order')

    return redirect('/')


@login_required(login_url='/auth/login')
def user_open_order(request, *args, **kwargs):
    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    coppone = Coppone(request.POST or None)
    discount_coppone = 0
    has_coppone = False
    has_coppone_message = False
    coppone_messages = ''
    if kwargs.get('is_paid') is not None:
        is_paid = True
    else:
        is_paid = False

    if coppone.is_valid():
        coppone_getter = coppone.cleaned_data.get('coppone_input')
        coppone_m: Coppone_Model = Coppone_Model.objects.filter(title=coppone_getter, active=True).first()
        if coppone_m is not None and open_order is not None:
            coppone_max = coppone_m.max_used
            coppone_current = coppone_m.current_used
            if coppone_current < coppone_max:
                coppone_current += 1
                coppone_m.current_used = coppone_current
                coppone_m.save()
                discount_coppone = coppone_m.percent
                has_coppone = True
                has_coppone_message = False
            elif coppone_current >= coppone_max:
                coppone_m.active = False
                coppone_m.save()
                discount_coppone = 101
                has_coppone = False
                has_coppone_message = True
                coppone_messages = 'ظرفیت استفاده از این کد به اتمام رسیده است'
                has_coppone_message = True

        elif open_order is None:
            has_coppone_message = True
            coppone_messages = 'شما هیچ سبد خریدی ندارید '

        elif coppone_m is None:
            has_coppone_message = True
            coppone_messages = 'هیچ کد تخفیفی با این نام پیدا نشده است'

        else:
            raise Http404('مشکلی پیش امده است لطفا انرا به مدران سایت اطلاع بدهید')

    context = {
        'has_coppone': False,
        'coppone': coppone,
        'order': None,
        'details': None,
        'maliat': SiteSetting.objects.first().maliat,
        'total': 0,
        'taxt': 0,
        'traveld': 0, 
        'finall_total': 0,
        'discount': discount_coppone,
        'discount_amount': 0,
        'coppone_messages': coppone_messages,
        'has_coppone_message': has_coppone_message,
        'can_paid': False,
        'is_paid': is_paid,
        }
    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()

    if open_order is not None:
        context['can_paid'] = True
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
        context['total'] = open_order.get_total_price()
        maliat = SiteSetting.objects.first().maliat
        if maliat > 0:
            percent = maliat / 100
            text = context['total'] * percent
            context['taxt'] = text

        discount = context['discount']
        if discount > 0:
            percent_discount = discount / 100
            text_discount = context['total'] * percent_discount
            context['discount_amount'] = text_discount
            context['has_coppone'] = has_coppone

        finall_total = context['traveld'] + context['taxt'] + context['total'] - context['discount_amount']
        context['finall_total'] = finall_total
        open_order.total_price = finall_total
        open_order.save()

        if context['traveld'] == 0:
            context['traveld'] = "رایگان"
    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        context['can_paid'] = True
    else:
        context['can_paid'] = False
    print(context['is_paid'])
    return render(request, 'order.html', context)


@login_required(login_url='/auth/login')
def remove_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        try:
            order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
            if order_detail is not None:
                order_detail.delete()
            else :
                Http404()
        except:
            Http404('')        
        
    return redirect('user_open_order')



# MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
# amount = 1000  # Toman / Required
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# email = 'maryus19915123@gmail.com'  # Optional
# mobile = '09373061991'  # Optional

# client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
# CallbackURL = 'http://localhost:8000/verify/'  # Important: need to edit for really server.


def send_request(request):
    print('send_request')
    return redirect('verify')

    # open_order = Order.objects.filter(owner_id = request.user.id, is_paid = False).first()
    # if open_order in not None:
    #     total_price = open_order.get_total_price()
    #     result = client.service.PaymentRequest(
    #                                             MERCHANT, total_price,
    #                                             description,
    #                                             email,
    #                                             mobile,
    #                                             CallbackURL + str(open_order.id)
    #                                             )

    #     if result.Status == 100:
    #         return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    #     else:
    #         raise Http404('درخواست شما لغو شد لطفا دوباره امتحان کنید و نگران نباشید چون که درخواست خرید شما لغو شد و پولتان به کارت شما بر می گردد')
    # else :
    #     raise Http404('درخواست شما لغو شد لطفا دوباره امتحان کنید و نگران نباشید چون که درخواست خرید شما لغو شد و پولتان به کارت شما بر می گردد')


def verify(request, *args, **kwargs):
    user_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()

    user_order.payment_date = datetime.datetime.now()
    user_order.refid = random.randint(100_000_000, 999_999_999)
    user_order.is_paid = True
    user_order.save()
    # kwargs['is_paid'] = True

    return redirect('user_open_order/True')

    # # order_id = kwargs.get('order_id')
    # user_order = Order.objects.get_queryset().get(owner_id = order_id, is_paid = False)
    # if request.GET.get('Status') == 'OK':
    #     result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], user_order.get_total_price())
    #     if result.Status == 100:
    #         user_order.is_paid = True
    #         user_order.payment_date = time.time()
    #         user_order.save()
    #         return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
    #     elif result.Status == 101:
    #         return HttpResponse('Transaction submitted : ' + str(result.Status))
    #     else:
    #         return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    # else:
    #     return HttpResponse('Transaction failed or canceled by user')
