from typing import Set, Union

from django.urls import path, URLResolver, URLPattern
from .views import ProductSearchListByTagOK

urlpatterns = [
    # path('', productListByTag.as_view()),
    path('<tagslug>', ProductSearchListByTagOK.as_view()),
]
