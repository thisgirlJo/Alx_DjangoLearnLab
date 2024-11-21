from django.urls import path, include
from . import views
#from .views import BookListView
from .views import list_books
from .views import register, custom_logout_view
#User Authentication for Login, Logout and Signup
#from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

#URLConf
urlpatterns = [
    #path('book/', views.list_books, name='books'),
    #path('library/', LibraryDetailView.as_view, name='library'),
    #User Auth
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    #path("register/", SignUpView.as_view(), name="templates/registration/signup"),
]