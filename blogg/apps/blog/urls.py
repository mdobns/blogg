from django.contrib import admin
from django.urls import path


from .views import edit_post_save, homepage, post_detail ,edit_post

urlpatterns = [
   path('', homepage, name='homepage'),
   path('post/<int:post_id>/', post_detail, name='post_detail'),
   path('post/<int:post_id>/edit/', edit_post, name='edit_post'),
   path('post/<int:post_id>/edit/save/', edit_post_save, name='edit_post_save'),
]