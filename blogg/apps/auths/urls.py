from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('myprofile/', views.my_profile, name='my_profile'),
    path('logout/', views.logout_view, name='logout'),
]