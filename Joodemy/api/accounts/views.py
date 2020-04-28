from rest_framework import viewsets, mixins

from accounts.models import User
from .serializers import UserSerializer


class UserRegistrationViewSet(mixins.CreateModelMixin,
                              viewsets.GenericViewSet,):
    """ User Registration """
    queryset = User.objects.all()
    serializer_class = UserSerializer
