from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Seller

@receiver(post_save, sender=CustomUser)
def create_related_profiles(sender, instance, created, **kwargs):
    """
    Automatically create related profiles based on the user's role.
    """
    if created:
        if instance.role == "seller":
            Seller.objects.create(user=instance)
        # if you later add Shopper or Admin models, handle them here too
        # elif instance.role == "shopper":
        #     Shopper.objects.create(user=instance)
        # elif instance.role == "admin":
        #     AdminProfile.objects.create(user=instance)
