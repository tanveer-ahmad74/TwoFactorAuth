from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


def validate_otp_number(value):
    if not 100000 <= value <= 999999:
        return ValidationError('Your otp is incorrect')
    else:
        return value


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=5)
    mobile_number = models.IntegerField(unique=True)
    otp = models.PositiveIntegerField(validators=[validate_otp_number], null=True, blank=True)
    is_verify = models.BooleanField(default=False)   # when user enter otp and match this will be True

    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "mobile_number"

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
