from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import ProductCategory


# class ProductCategoryAdmin(admin.ModelAdmin):
#     list_display = ['__str__', 'name']
#
#     class Meta:
#         model = ProductCategory


admin.site.register(ProductCategory, DraggableMPTTAdmin,
                    list_display=[
                        'tree_actions',
                        'indented_title'
                    ],
                    list_display_links=[
                        'indented_title',
                    ]
                    )




