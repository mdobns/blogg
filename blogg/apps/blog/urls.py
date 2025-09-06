from django.contrib import admin
from django.urls import path


from .views import homepage, post_detail

urlpatterns = [
   path('', homepage, name='homepage'),
   path('post/<int:post_id>/', post_detail, name='post_detail'),
]