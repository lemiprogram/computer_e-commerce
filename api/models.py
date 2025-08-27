
from django.db import models
from django.conf import settings
from exposed_wires_app.models import Product, Shopper

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