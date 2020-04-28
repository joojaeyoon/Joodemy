from rest_framework import status, viewsets
from rest_framework.response import Response

from accounts.models import Instructor
from course.models import Content, Course, Review

from .serializers import *


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):

        kwargs['context'] = self.get_serializer_context()
        serializer = CourseCreateSerializer(data=request.data, **kwargs)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        i_id = serializer.data["instructor"]
        username = Instructor.objects.filter(
            id=i_id)[0].user.username

        response = serializer.data.copy()
        response["instructor"] = username

        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
