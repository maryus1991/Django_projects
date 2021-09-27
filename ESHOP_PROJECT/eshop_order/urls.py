from django.urls import path
from eshop_order.views import ( add_user_order,
                                user_open_order,
                                send_request,
                                verify,
                                remove_order_detail
)

urlpatterns = [
    path('add_user_order', add_user_order, name='add_user_order'),
    path('user_open_order/<is_paid>', user_open_order),
    path('user_open_order', user_open_order, name='user_open_order'),
    path('remove_order_detail/<detail_id>', remove_order_detail, name='remove_order_detail'),
    path('request', send_request, name='request'),
    path('verify', verify, name='verify'),
]
