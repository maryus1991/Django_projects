from django.urls import path
from .views import favorate_page, add_favorate_item, remove_favorate_item

urlpatterns = [
    path('favorate-page', favorate_page, name='favorate_page'),
    path('add-favorate-item', add_favorate_item, name='add_favorate_item'),
    path('remove_favorate_item/<removeid>', remove_favorate_item, name='remove_favorate_item'),
]