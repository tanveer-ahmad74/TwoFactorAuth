from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import UserViewSet, VerifyOTP, GenerateOTP

router_master = DefaultRouter()
router_master.register('user', UserViewSet, basename="user")


urlpatterns = [
    path('', include(router_master.urls)),
    path('verify/', VerifyOTP.as_view(), name='verify'),
    path('get-otp/', GenerateOTP.as_view(), name='get-otp')

]