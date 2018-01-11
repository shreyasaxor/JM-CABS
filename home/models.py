from django.db import models
import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=UserManager.normalize_email(email))
        user.first_name = first_name
        user.email = email
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password):
        user = self.create_user(email=email,
                                first_name=first_name, password=password)
        user.email = email
        user.first_name = first_name
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class contact_info(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.IntegerField(null=True)
    message=models.CharField(max_length=250)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, default='123')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    objects = UserManager()
