from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductList.as_view()),
    path('category/<category_name>', ProductListByCategory.as_view()),
    path('<productid>/<title>', product_detail),
    path('search', SearchProductView.as_view()),
    path('products_categories_partial', products_categories_partial, name='products_categories_partial')
]

