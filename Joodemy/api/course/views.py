from rest_framework import status, viewsets
from rest_framework.response import Response

from accounts.models import Instructor, User
from course.models import Content, Course, Review

from .serializers import *


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CourseCreateSerializer

        return self.serializer_class

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
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

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ContentCreateSerializer

        return self.serializer_class

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        c_id = serializer.data["course"]
        title = Course.objects.filter(
            id=c_id)[0].title

        response = serializer.data.copy()
        response["course"] = title

        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ReviewCreateSerializer

        return self.serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        c_id = serializer.data["course"]
        u_id = serializer.data["user"]
        title = Course.objects.filter(
            id=c_id)[0].title
        username = User.objects.filter(id=u_id)[0].username

        response = serializer.data.copy()
        response["course"] = title
        response["user"] = username

        return Response(response, status=status.HTTP_201_CREATED, headers=headers)
