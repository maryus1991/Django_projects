from django.contrib import admin
from eshop_order.models import Order, OrderDetail, Coppone_Model


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)
admin.site.register(Coppone_Model)
