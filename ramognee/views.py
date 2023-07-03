from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, serializers, generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
from .models import *
from .serializers import *

# Create your views here.

UserModel = get_user_model()

class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    http_method_names = ['post']

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = UserModel.objects.get(user_phone_no=request.data['user_phone_no'])
        return Response({"message": "User Registered", "data": self.get_tokens(user)}, status=status.HTTP_200_OK)

    def get_tokens(self, user):
            refresh = RefreshToken.for_user(user)
            return {
                'user': {'phone': user.user_phone_no},
                'access': str(refresh.access_token),
                }

class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer
    http_method_names = ['post']

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserModel.objects.get(user_phone_no=request.data['user_phone_no'])
        return Response({"message": "Logged-In Successfully", "data": self.get_tokens(user)}, status=status.HTTP_200_OK)

    def get_tokens(self, user):
            refresh = RefreshToken.for_user(user)
            return {
                'user': {'phone': user.user_phone_no},
                'access': str(refresh.access_token),
                }
    