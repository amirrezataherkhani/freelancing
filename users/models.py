from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from users.managers import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    username = None
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    cart_number = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.user.email
