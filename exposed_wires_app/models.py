
from django.db import models
from registration.models import CustomUser
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Shopper(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="shopper_profile")
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    profile_image = CloudinaryField('image', blank=True, null=True)
    def __str__(self):
        return f"Shopper: {self.user.username}"
    
class Seller(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="seller_profile")
    store_name = models.CharField(max_length=100)
    store_description = models.TextField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return f"Seller: {self.store_name}"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = CloudinaryField('image', blank=True, null=True)
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
class Condition(models.Model):
    condition = models.CharField(max_length=32,null=True,unique=True)
    
    class Meta:
        ordering = ["-condition"]

    def __str__(self):
        return self.name

class Product(models.Model):
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name="products"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
        blank=True
    )
    condition = models.ForeignKey(
        Condition,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = CloudinaryField("image", blank=True, null=True)
    extra_images = ArrayField(CloudinaryField("image", blank=True, null=True),blank=True, null=True)
    deal = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)], default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name