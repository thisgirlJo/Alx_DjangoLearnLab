from django.urls import path
from . import views
#from .views import BookListView
from .views import list_books
from .views import signup
#User Authentication for Login, Logout and Signup
from django.contrib.auth import views as auth_views

#URLConf
urlpatterns = [
    #path('book/', views.list_books, name='books'),
    #path('library/', LibraryDetailView.as_view, name='library'),
    #User Auth
    path('/registration/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.register. LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.signup, name='register'),
]