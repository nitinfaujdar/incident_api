from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, serializers, generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
import random as r
import datetime
from .models import *
from .serializers import *

# Create your views here.

UserModel = get_user_model()

class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    http_method_names = ['post']

    def post(self, request):
        user = UserModel.objects.filter(username=request.data['username'])
        if user.exists():
            raise serializers.ValidationError({"error_message":"This Username already exist"})
        user = UserModel.objects.filter(Q(country_code=request.data['country_code']) 
                                        & Q(user_phone_no=request.data['user_phone_no']))
        if user.exists():
            raise serializers.ValidationError({"error_message":"This phone number already exist"})    
        user = UserModel.objects.filter(user_email=request.data['user_email'])
        if user.exists():
            raise serializers.ValidationError({"error_message":"This email ID already exist"})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = UserModel.objects.get(user_phone_no=request.data['user_phone_no'])
        return Response({"message": "User Registered", "data": self.get_tokens(user)}, status=status.HTTP_200_OK)

    def get_tokens(self, user):
            refresh = RefreshToken.for_user(user)
            return {
                'user': {'username': user.username},
                'access': str(refresh.access_token),
                }

class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer
    http_method_names = ['post']

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserModel.objects.filter(Q(country_code=request.data['country_code']) 
                                        & Q(user_phone_no=request.data['user_phone_no']))
        if not user.exists():
            raise serializers.ValidationError({"error_message":"User Does not exist"})   
        user = UserModel.objects.get(user_phone_no=serializer.data['user_phone_no'])
        if not user.check_password(serializer.data['password']):
            raise serializers.ValidationError({"error_message":"Invalid Authentication Credentials"})
        return Response({"message": "Logged-In Successfully", "data": self.get_tokens(user)}, status=status.HTTP_200_OK)

    def get_tokens(self, user):
            refresh = RefreshToken.for_user(user)
            return {
                'user': {'username': user.username},
                'access': str(refresh.access_token),
                }

class ProfileView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    http_method_names = ['get']

    def get(self, request):
        obj = UserModel.objects.get(id=request.user.id)
        serializer = self.get_serializer(obj)
        return Response({"message": "Profile fetched Successfully", "data": serializer.data}, status=status.HTTP_200_OK)
    
def generate_incident_id():
        id="RMG"
        for i in range(5):
            id+=str(r.randint(1,9))
        return id + str(datetime.datetime.now().year)

class IncidentView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = IncidentSerializer

    def post(self, request):
        request.data['user'] = request.user.id
        request.data['incident_id'] = generate_incident_id()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Incident added Successfully", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def get(self, request):
        obj = Incident.objects.filter(user=request.user)
        serializer = self.get_serializer(obj, many=True)
        return Response({"message": "Incidents fetched Successfully", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request):
        try:
            obj = Incident.objects.get(id = request.data['id'])
        except Incident.DoesNotExist:
            raise serializers.ValidationError({
                  "error_message": "Invalid Incident ID supplied!.."
             })
        if obj.incident_status != 'CLOSED':
            obj.incident_details = request.data['incident_details']
            obj.priority = request.data['priority']
            obj.incident_status = request.data['incident_status']
            obj.save()
            serializer = self.get_serializer(obj)
            return Response({"message": "Incidents updated Successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            raise serializers.ValidationError({
                 "error_message": "Incident can't be updated"
            })

class GetIncidentByIDView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = IncidentSerializer
    
    def get(self, request):
        incident_id = request.query_params.get('incident_id')
        try:
            obj = Incident.objects.get(incident_id=incident_id)
        except Incident.DoesNotExist:
            raise serializers.ValidationError({
                  "error_message": "Invalid Incident ID supplied!.."
             })
        serializer = self.get_serializer(obj)
        return Response({"message": "Incident fetched Successfully", "data": serializer.data}, status=status.HTTP_200_OK)

