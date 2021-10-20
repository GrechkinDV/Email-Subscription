from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionViewset(ModelViewSet):
    """
    A modelviewset for Email Subscriptions 
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    http_method_names = ["get", "post", "delete"]
