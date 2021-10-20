from rest_framework.serializers import ModelSerializer

from .models import Subscription


class SubscriptionSerializer(ModelSerializer):
    """
    Serializer for Subscription Model
    """
    class Meta:
        model = Subscription
        fields = "__all__"
