from django.db import models
from registration.models import CustomUser
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField

class  Filter(models.Model):
    key = models.CharField(max_length=32, null=True)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = CloudinaryField("image", blank=True, null=True)
    filters = models.ManyToManyField(Filter,null=True)
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Condition(models.Model):
    condition = models.CharField(max_length=32, null=True, unique=True)

    class Meta:
        ordering = ["-condition"]

    def __str__(self):
        return self.condition


class Store(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Shopper(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="shopper_profile")
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    profile_image = CloudinaryField("image", blank=True, null=True)

    def __str__(self):
        return f"Shopper: {self.user.username}"


class Seller(models.Model):
    STORE_ROLES = [
        ('None','None'),
        ('Staff','Staff'),
        ('Admin','Admin'),

    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="seller_profile")
    store = models.OneToOneField(Store, on_delete=models.CASCADE, related_name="seller", null=True, blank=True)
    store_role = models.CharField(max_length=16, choices=STORE_ROLES, default="None")
    city = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = CloudinaryField("image", blank=True, null=True)

    def __str__(self):
        return f"Seller: {self.user.username} - {self.store.name if self.store else 'No Store'}"


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", null=True, blank=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name="products", null=True, blank=True)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = CloudinaryField("image", blank=True, null=True)
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
        null=True
    )
    clicks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-clicks',"-discount",'price',"-created_at"]


    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    shopper = models.ForeignKey(Shopper, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # auto-calc total price if not set
        if not self.total_price:
            self.total_price = self.product.get_deal() * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name} x{self.quantity}"
class Cart(models.Model):
    shopper = models.OneToOneField(
        Shopper,  # or settings.AUTH_USER_MODEL if Shopper extends CustomUser
        on_delete=models.CASCADE,
        related_name="cart"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.subtotal() for item in self.items.all())

    def __str__(self):
        return f"Cart ({self.shopper})"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

class Wishlist(models.Model):
    shopper = models.ForeignKey(
        Shopper, 
        on_delete=models.CASCADE,
        related_name="wishlist"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="wishlisted_in"
    )
    added_at = models.DateTimeField(auto_now_add=True)  
    class Meta:
        ordering = ["-added_at"]

    def __str__(self):
        return f"{self.user.username}'s Wishlist - {self.product.name}"
