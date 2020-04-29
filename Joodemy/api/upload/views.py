from rest_framework import status, views
from rest_framework.response import Response

from .serializers import *

from django.views.decorators.csrf import csrf_exempt


class ImageUploadView(views.APIView):

    def post(self, request, foramt=None):

        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoUploadView(views.APIView):

    def post(self, request, foramt=None):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
