# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('shopper', 'Shopper'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
    ]

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='shopper')
    
    date_joined = models.DateField(auto_now=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username or self.email
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        # Import inside method to avoid circular import
        from exposed_wires_app.models import Seller,Shopper

        if is_new:
            if self.role == "shopper":
                Shopper.objects.create(user = self)
            if self.role == "seller":
                Seller.objects.create(user = self)