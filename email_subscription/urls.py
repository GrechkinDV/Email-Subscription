from django.urls import path, include

from rest_framework import routers

from .views import SubscriptionViewset


router = routers.SimpleRouter()
router.register(r"", SubscriptionViewset)

urlpatterns = [
    path(r"", include(router.urls)),
]
