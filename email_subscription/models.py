from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from .utils import send_subscription_success


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_date = models.DateTimeField(auto_now_add=True)


# method for sending email
@receiver(post_save, sender=Subscription)
def update_stock(sender, instance, **kwargs):
    send_subscription_success(instance.email)
