from django.urls import path
from . import views
from .views import UserLoginView, User_CustomView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserLoginView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]