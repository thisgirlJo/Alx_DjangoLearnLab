from django.urls import path
from . import views
from .views import register, login


urlpatterns = [
    path('register/', views.register, name='Register'),
    path('login/', views.login, name='Login'),
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]