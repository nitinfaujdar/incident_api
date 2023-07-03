from django.core.validators import MinLengthValidator
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

UserModel = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    user_email = serializers.CharField(required=True)
    user_phone_no = serializers.CharField(required=True)
    password = serializers.CharField(validators=[MinLengthValidator(8)], required=True, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'user_phone_no', 'user_email']

    def validate_username(self, attrs):
        user = UserModel.objects.filter(username=attrs['username'])
        if user.exists():
            raise serializers.ValidationError({"error_message":"This Username already exist"})
        return attrs
    
    def validate_phone(self, attrs):
        user = UserModel.objects.filter(user_phone_no=attrs['user_phone_no'])
        if user.exists():
            raise serializers.ValidationError({"error_message":"This phone number already exist"})
        return attrs
    
    def validate_email(self, attrs):
        user = UserModel.objects.filter(user_email=attrs['user_email'])
        if user.exists():
            raise serializers.ValidationError({"error_message":"This email ID already exist"})
        return attrs

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            user_phone_no=validated_data['user_phone_no'],
            user_email=validated_data['user_email'],
            password=validated_data['password'],
        )
        user = UserModel.objects.get(user_phone_no=validated_data['user_phone_no'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    user_phone_no = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['user_phone_no', 'password']
    
    def validate_user(self, attr):
        user = UserModel.objects.filter(user_phone_no=attr['user_phone_no'])
        if not user.exists():
            raise serializers.ValidationError({"error_message":"User Does not exist"})
        return attr     
    
    def validate_password(self, attr):
        user = UserModel.objects.get(user_phone_no=attr['user_phone_no'])
        if user.check_password == attr['password']:
            raise serializers.ValidationError({"error_message":"Invalid Authentication Credentials"})
        return attr
