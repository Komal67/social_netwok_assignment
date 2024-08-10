from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import FriendRequest, Friend


@receiver(post_save, sender=FriendRequest)
def create_friends_instance(sender, instance, **kwargs):
    if instance.status == 'accepted':
        Friend.objects.create(user=instance.requester, friend=instance.recipient)
        Friend.objects.create(user=instance.recipient, friend=instance.requester)