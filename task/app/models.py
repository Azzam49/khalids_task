from django.db import models

# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from task.app.common.text_choices.user_types import UserTypeOption

class CustomUserManager(BaseUserManager):
    """Manager For User Profiles"""

    def create_user(self, email, commercial_num, password=None):
        """Create a new user profile """
        if not email:
            raise ValueError('User Must Have an Email Address')
        email = self.normalize_email(email)
        user = self.model(email=email, commercial_registration_num=commercial_num)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, commercial_registration_num, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, commercial_registration_num, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Database model For Users in the System"""
    email = models.EmailField(max_length=255, unique=True)
    user_type = models.CharField(max_length=20, choices=UserTypeOption.choices, null=True, blank=True)
    commercial_registration_num = models.CharField(max_length=50, unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'commercial_registration_num'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = "User"

    def __str__(self):
        """Return String Representation of our user """
        return self.email
