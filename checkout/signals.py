from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem, ProgOrderLineItem


@receiver(post_save, sender=OrderLineItem)
@receiver(post_save, sender=ProgOrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    [Code taken from Code Institute and modified for personal use]
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
@receiver(post_delete, sender=ProgOrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    [Code taken from Code Institute and modified for personal use]
    """
    instance.order.update_total()
