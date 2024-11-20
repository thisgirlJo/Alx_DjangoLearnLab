from django.urls import path
from . import views
#from .views import BookListView
from .views import list_books
from .views import signup
#User Authentication for Login, Logout and Signup
#from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

#URLConf
urlpatterns = [
    path('book/', views.list_books, name='books'),
    path('library/', LibraryDetailView.as_view, name='library'),
    #User Auth
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    #path("register/", SignUpView.as_view(), name="templates/registration/signup"),
]