from django.urls import path
from .views import add_comments, edit_comments

urlpatterns = [
    path('add-comments', add_comments, name='add_comments'),
    path('edit-comments', edit_comments, name='edit_comments'),
]
