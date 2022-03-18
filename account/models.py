from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

#связь с БД

class UserManager(BaseUserManager):
    def _create(self, email, password, name, last_name, **extra_fields):
        if not email:
            raise ValueError('Email cannot be empty')
        user = self.model(email=email, name=name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, name, last_name, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        return self._create(email, password, name, last_name, **extra_fields)

    def create_superuser(self, email, password, name, last_name, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(email, password, name, last_name, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name']

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj):
        return self.is_staff

    @staticmethod
    def generate_activation_code():
        from django.utils.crypto import get_random_string
        code = get_random_string(8)
        return code

    def set_activation_code(self):
        code = self.generate_activation_code()
        if User.objects.filter(code=code).exits():
            self.set_activation_code()
        else:
            self.activation_code = code
            self.save()



