from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class IsActiveModel(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

# Create your models here.
class User(AbstractUser, PermissionsMixin, IsActiveModel):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name