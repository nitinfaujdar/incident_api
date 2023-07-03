from django.core.validators import MinLengthValidator
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

UserModel = get_user_model()

class RecruiterRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    password = serializers.CharField(validators=[MinLengthValidator(8)], required=True, write_only=True)

    class Meta:
        model = User
        fields = ['__all__']

    def validate_phone(self, attrs):
        user = UserModel.objects.filter(Q(phone=attrs))
        if user.exists():
            raise serializers.ValidationError({"error_message":"This phone number already exist"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            user_phone_no=validated_data['user_phone_no'],
            user_email=validated_data['user_email'],
            password=validated_data['password'],
        )
        return user