from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import register, profile_view, home_view, base_view

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('base/', views.base_view, name='base'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
