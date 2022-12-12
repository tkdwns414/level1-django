from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import User
from products.models import Cart

@receiver(post_save, sender=User)
def user_post_save(sender, instance):
    Cart.objects.create(user=instance)