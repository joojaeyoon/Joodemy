from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny

from accounts.models import User
from .serializers import UserSerializer


from rest_auth.serializers import JWTSerializer
from rest_auth.utils import jwt_encode


class UserRegistrationViewSet(mixins.CreateModelMixin,
                              viewsets.GenericViewSet,):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication, ]
    permission_classes = [AllowAny, ]

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        token = jwt_encode(user)

        data = {
            'user': user,
            'token': token
        }
        serializer = JWTSerializer(instance=data,
                                   context={'request': self.request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)
