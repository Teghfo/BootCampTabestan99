from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, phone, email, password=None, is_staff=False, is_superuser=False, **kwargs):
        """
        customize user to have email as token
        """
        if not email:
            raise ValueError('email ro mikham')

        if not password:
            raise ValueError('password ro mikham')

        if not phone:
            raise ValueError('phone ro mikham')

        user = self.model(phone=phone, email=self.normalize_email(email))

        user.set_password(password)
        user.staff = is_staff
        user.superuser = is_superuser

        user.save()

        return user

    def create_superuser(self, phone, email, password, is_staff=True, is_superuser=True):
        return self.create_user(
            phone=phone,
            email=email,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser
        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    time_created = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser
