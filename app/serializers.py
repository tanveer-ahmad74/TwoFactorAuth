from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile_number', 'password', 'is_verify']
        read_only_fields = ['otp', 'is_verify']


class GenerateOTPSerializer(serializers.Serializer):
    mobile_number = serializers.CharField()


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['otp']
