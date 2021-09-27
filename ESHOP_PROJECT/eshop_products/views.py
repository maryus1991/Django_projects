from django.shortcuts import render
from django.views.generic import ListView
from eshop_account.models import VisitCount
from eshop_order.forms import UserNewOrder
from eshop_favorate.forms import FavorateItem
from .models import Product, ProductGallery
from django.http import Http404
from eshop_products_category.models import ProductCategory
import itertools
from eshop_comments.forms import CommentsForms, SubmitForEditCommentsForms, EditCommentsForms
from eshop_comments.models import Comments


# Create your views here.


class ProductList(ListView):
    template_name = 'product.html'
    paginate_by = 12

    def get_queryset(self):
        return Product.objects.get_active_product()


class ProductListByCategory(ListView):
    template_name = 'product.html'
    paginate_by = 12

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = Product.objects.get_products_by_category(category_name)
        if category is None:
            raise Http404('صفحه مورد نظر یافت نشد')

        return Product.objects.get_products_by_category(category_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def product_detail(request, *args, **kwargs):
    productid = kwargs['productid']
    # title = kwargs['title']
    gallery = ProductGallery.objects.filter(product_id=productid)
    new_order_form = UserNewOrder(request.POST or None, initial={'productid': productid})
    comments_form = CommentsForms(request.POST or None, initial={'productid': productid})
    if request.user.is_authenticated:
        if request.user.get_full_name() is not None and request.user.get_full_name() != '':
            full_name_of_user_or_username = request.user.get_full_name()
        else:
            full_name_of_user_or_username = request.user.username

        comments_form = CommentsForms(request.POST or None, initial={
            'productid': productid,
            'email': request.user.email,
            'full_name': full_name_of_user_or_username
        })

    submitforeditCommentsforms = SubmitForEditCommentsForms(request.POST or None)
    # editfromforcomments = EditCommentsForms(request.POST or None)
    # print(submitforeditCommentsforms.is_valid())
    if submitforeditCommentsforms.is_valid():
        commentid = submitforeditCommentsforms.cleaned_data.get('commentid')
        comments = Comments.objects.filter(id=commentid).first()

        editfromforcomments = EditCommentsForms(request.GET or None, initial={
            'commentid': commentid,
            'productid': productid,
            'email': comments.email,
            'full_name': comments.full_name,
            'text': comments.text,
        })
        comments_form = editfromforcomments

    new_favorate_form = FavorateItem(request.POST or None, initial={'pk': productid})
    product: Product = Product.objects.get_by_id(productid)
    tags = product.tag_set.all()
    galleries_listed = list(my_grouper(3, gallery))
    product_comments = Comments.objects.filter(product=product).all()

    visited_ip: VisitCount = VisitCount.objects.filter(ip=get_ip(request)).first()

    if request.user.is_authenticated:
        visited_ip: VisitCount = VisitCount.objects.filter(username=request.user.username, email=request.user.email,
                                                           user_id=request.user.id).first()
    # print(request.user.is_authenticated)
    ip_addr = get_ip(request)
    if visited_ip is None:
        if request.user.is_authenticated:
            VisitCount.objects.create(ip=ip_addr, email=request.user.email, username=request.user.username,
                                      user_id=request.user.id).products.add(product)
            product.visit_count += 1
            product.save()
        else:
            VisitCount.objects.create(ip=ip_addr).products.add(product)
            product.visit_count += 1
            product.save()

    elif visited_ip is not None:
        product_list_from_visited_ip = visited_ip.products.all()
        if product not in product_list_from_visited_ip:
            visited_ip.products.add(product)
            visited_ip.save()
            product.visit_count += 1
            product.save()
    else:
        # TODO : add a notifications for error
        pass

    related_product = Product.objects.get_queryset().filter(category__product=product).distinct()
    related_product_grouped = list(my_grouper(3, related_product))

    if product is None:
        raise Http404('این محصول یافت نشد')
    elif not product.active:
        raise Http404('این محصول یافت نشد')

    if product is not None and product.active:
        context = {
            'product': product,
            'tags': tags,
            'galleries': galleries_listed,
            'related_product': related_product_grouped,
            'visit_count': product.visit_count,
            'new_favorate_form': new_favorate_form,
            'new_order_form': new_order_form,
            'comments_form': comments_form,
            'product_comments': product_comments,
            # 'editfromforcomments': editfromforcomments,
            'SubmitForEditCommentsForms': SubmitForEditCommentsForms(request.POST or None),
        }
        return render(request, 'product_details.html', context)
    else:
        return Http404()


class SearchProductView(ListView):
    template_name = 'product.html'
    paginate_by = 12

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        print(query)
        if query is not None:
            return Product.objects.search(query)
        else:
            return Product.objects.none()


def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories_product_partial.html', context)
