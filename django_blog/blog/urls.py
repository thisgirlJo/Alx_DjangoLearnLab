from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views as auth_views

urlpatterns = [
    path('home/', auth_views.profile_view, name='Home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', auth_views.register, name='register'),
]
