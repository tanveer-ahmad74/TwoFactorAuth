from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.contrib.auth import get_user_model
from app.serializers import UserSerializer, OTPSerializer, GenerateOTPSerializer
from random import randrange
from django.contrib.auth.hashers import make_password
User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pasw = request.data.get('password')
        password = make_password(pasw)
        username = request.data.get('username')
        email = request.data.get('email')
        mobile_number = request.data.get('mobile_number')
        serializer.save(username=username, email=email, password=password,
                        mobile_number=mobile_number)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenerateOTP(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = GenerateOTPSerializer
    throttle_scope = 'otp'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = self.request.user.username
        mobile_number = request.data.get('mobile_number')
        user = User.objects.get(username=username, mobile_number=mobile_number)
        if user:
            otp = randrange(100000, 999999)
            return Response({'message': 'Copy the otp it will not show it again if you refresh it', 'Otp': otp})
        else:
            return Response({'message': 'mobile number does not exist'})


class VerifyOTP(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = OTPSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        OTP = request.data['otp']
        if len(OTP) != 0 and len(OTP) == 6:
            username = self.request.user.username
            user = User.objects.filter(username=username, otp=OTP).first()
            if user is not None:
                user.is_verify = True
                user.save()
                return Response({'message': 'User Verify'})
            else:
                return Response({'message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'please enter correct otp'}, status=status.HTTP_406_NOT_ACCEPTABLE)
