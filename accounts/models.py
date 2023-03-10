from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("کاربر باید ایمیل آدرس داشته باشد")
        if not username:
            raise ValueError("کاربر باید دارای نام کاربری باشد")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self , email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user

class UserType(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=300, unique=True)
    username = models.CharField(max_length=255)
    user_type = models.ManyToManyField(UserType, related_name="user_type")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="media/user/images", null=True, blank=True)


    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.email
    

    def get_email(self):
        return self.email


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    district = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255,null=True, blank=True)
    house_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username } From { self.country}"
