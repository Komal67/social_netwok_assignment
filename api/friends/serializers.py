
from rest_framework import serializers

from .models import FriendRequest, Friend


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = []

