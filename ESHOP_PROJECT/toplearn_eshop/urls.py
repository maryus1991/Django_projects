from django.conf.urls.static import static
from django.contrib import admin
from django_tools.middlewares import ThreadLocal
from django.urls import path, include
from . import settings
from .views import *

print(ThreadLocal.get_current_user())

urlpatterns = [
    path('404', notfound),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('', home_page),
    path('about-us', about_page),
    path('auth/', include('eshop_account.urls')),
    path('product/', include('eshop_products.urls')),
    path('', include('eshop_contact.urls')),
    path('order/', include('eshop_order.urls')),
    path('favorates/', include('eshop_favorate.urls')),
    path('admin/', admin.site.urls),
    path('tag/', include('eshop_tag.urls')),
    path('comments/', include('eshop_comments.urls')),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
