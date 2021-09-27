from django.contrib import admin
from .models import ContactUs


class ContactAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'subject', 'is_read']
    list_filter = ['is_read', 'subject']
    list_editable = ['is_read']
    search_fields = ['fullname', 'email', 'subject', 'text']


admin.site.register(ContactUs, ContactAdmin)