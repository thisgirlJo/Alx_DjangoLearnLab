from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import User_CustomSerializer, UserLoginSerializer, CustomTokenObtainPairSerializer

# Create your views here.
class User_CustomView(APIView):
    def post(self, request):
        serializer = User_CustomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer