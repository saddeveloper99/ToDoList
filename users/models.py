from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

# 유저 생성기능을 관리하는 클래스


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# 유저 객체의 필드들을 정의해줄 클래스
class CustomUser(AbstractBaseUser):
    email = models.EmailField("email address", max_length=255, unique=True,)
    name = models.CharField("name", max_length=20, unique=True)
    # password = models.CharField("password", max_length=20)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('B', 'Both'),
        ('U', 'unknown'),
    )
    # Male Female Unknown Both for their first Char
    gender = models.CharField(max_length=1, choices=gender_choices)
    age = models.PositiveIntegerField()
    bio = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
