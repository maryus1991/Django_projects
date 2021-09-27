from django.views.generic import ListView
from eshop_products.models import Product
from django.http import Http404


class ProductSearchListByTagOK(ListView):
    template_name = 'product.html'
    paginate_by = 12

    def get_queryset(self):
        tag_slug = self.kwargs['tagslug']
        products: Product = Product.objects.filter(tag__slug=tag_slug).distinct().all()
        if products is None:
            raise Http404('صفحه مورد نظر یافت نشد')

        return products
