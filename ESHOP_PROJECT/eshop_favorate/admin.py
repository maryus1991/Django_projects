from django.contrib import admin
from .models import FavorateItem, FavorateItemDetail

admin.site.register(FavorateItem)
admin.site.register(FavorateItemDetail)