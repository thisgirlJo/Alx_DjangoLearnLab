from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import register, profile_view, home_view, base_view, PostListView, PostCreateView, PostDeleteView, PostUpdateView, PostDetailView

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('base/', views.base_view, name='base'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('post/', PostListView.as_view()),
    path('post/new/', PostCreateView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view()),
    path('post/<int:pk>/delete/', PostDeleteView.as_view()),
    path('post/<int:pk>/update/', PostUpdateView.as_view())
]
