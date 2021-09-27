import datetime

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect
from .forms import CommentsForms, EditCommentsForms
from eshop_products.models import Product
from .models import Comments


@login_required(login_url='/auth/login')
def add_comments(request):
    commentsfrom = CommentsForms(request.POST or None)
    if commentsfrom.is_valid():
        full_name = commentsfrom.cleaned_data.get('full_name')
        email = commentsfrom.cleaned_data.get('email')
        text = commentsfrom.cleaned_data.get('text')
        pk = commentsfrom.cleaned_data.get("productid")
        product: Product = Product.objects.filter(id=pk).first()
        Comments.objects.create(full_name=full_name, email=email, text=text, product=product, owner=request.user)
        return redirect(product.get_absolute_url())
    else:
        raise Http404('مشکلی پیش امده است')


@login_required(login_url='/auth/login')
def edit_comments(request):
    editform = EditCommentsForms(request.POST or None)
    if editform.is_valid():
        full_name = editform.cleaned_data.get('full_name')
        pk = editform.cleaned_data.get('productid')
        commentid = editform.cleaned_data.get('commentid')
        email = editform.cleaned_data.get('email')
        text = editform.cleaned_data.get('text')
        product: Product = Product.objects.filter(id=pk).first()
        editedcommend: Comments = Comments.objects.filter(id=commentid, product=product, owner=request.user).first()
        if editedcommend is not None:
            editedcommend.email = email
            editedcommend.full_name = full_name
            editedcommend.text = text
            editedcommend.edited_date = datetime.datetime.now()
            editedcommend.edited = True
            editedcommend.save()
            return redirect(product.get_absolute_url())
        elif editedcommend is None:
            Comments.objects.create(full_name=full_name, email=email, text=text, product=product, owner=request.user)
            return redirect(product.get_absolute_url())
        else:
            raise Http404('مشکلی پیس امده است')

    raise Http404('مشکلی پیس امده است')
