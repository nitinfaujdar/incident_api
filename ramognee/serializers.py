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
        model = UserModel
        fields = ['type', 'username', 'first_name', 'last_name', 'country_code', 'user_phone_no', 
                  'user_email', 'address', 'pincode', 'country', 'state', 'city', 'password']

    def create(self, validated_data):
        user = UserModel.objects.create(
            type=validated_data['type'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
            pincode=validated_data['pincode'],
            country=validated_data['country'],
            state=validated_data['state'],
            city=validated_data['city'],
            country_code=validated_data['country_code'],
            user_phone_no=validated_data['user_phone_no'],
            user_email=validated_data['user_email'],
        )
        user = UserModel.objects.get(user_phone_no=validated_data['user_phone_no'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(required=True)
    user_phone_no = serializers.CharField(required=True)

    class Meta:
        model = UserModel
        fields = ['country_code', 'user_phone_no', 'password']

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['type', 'username', 'first_name', 'last_name', 'country_code', 'user_phone_no', 
                  'user_email', 'address', 'pincode', 'country', 'state', 'city']

class IncidentSerializer(serializers.ModelSerializer):
    reporting_person_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Incident
        fields = ['user', 'reporting_person_details', 'incident_id', 'incident_details', 'priority', 
                  'incident_status']
    
    def create(self, validated_data):
        obj = Incident.objects.create(
            user=validated_data['user'],
            incident_id=validated_data['incident_id'],
            incident_details=validated_data['incident_details'],
            priority=validated_data['priority'],
            incident_status=validated_data['incident_status'])
        return obj
    
    def get_reporting_person_details(self, usr: Incident):
        user = UserModel.objects.filter(id=usr.user.id).values()
        data = ProfileSerializer(user, many=True)
        return data.data
