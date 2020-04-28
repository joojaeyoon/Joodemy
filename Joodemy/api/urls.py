from django.urls import path, include

from rest_framework import routers

from .accounts.views import UserRegistrationViewSet

router = routers.DefaultRouter()
router.register(r"^", UserRegistrationViewSet)

app_name = "api"

urlpatterns = [
    path("auth/registration", include(router.urls)),
    path("auth/", include("rest_auth.urls")),
]
