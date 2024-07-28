"""
Database Models
"""

from django.db import models  # django ORM tool for defining models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    # **extra_fields is to pass any number of keyword arguemts
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        # ValueError is a built in exception, so we do not have to import it.
        if not email:
            raise ValueError('User must have an email address.')
        # normalize_email is a method on BaseUserManager calss which normalizes email addresses
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """create and resturn super user"""

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
