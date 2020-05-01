from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from accounts.models import Instructor, User
from course.models import Content, Course, Review

from ..utils import get_video_time
from .serializers import *
from ..upload.serializers import *


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def create_image(self, data):
        serializer = ImageSerializer(data=data)
        if serializer.is_valid():
            return serializer.save()
        return None

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CourseCreateSerializer

        return self.serializer_class

    def list(self, request, *args, **kwargs):
        instructor = request.query_params.get("instructor", None)

        if instructor != None:
            queryset = self.get_queryset().filter(instructor=instructor)
        else:
            queryset = self.get_queryset()

        print(queryset[0].img)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        data = request.data.copy()

        image = self.create_image({"image": data["img"]})

        user_id = data.get("instructor")
        instructor = Instructor.objects.filter(
            user__id=user_id)[0]

        data["img"] = image.id

        data["instructor"] = instructor.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        response = serializer.data.copy()
        response["instructor"] = instructor.user.username

        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def create_video(self, data):
        serializer = VideoSerializer(data=data)
        if serializer.is_valid():
            return serializer.save()
        return None

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ContentCreateSerializer

        return self.serializer_class

    def create(self, request, *args, **kwargs):

        video = self.create_video({"video": request.data["video"]})

        request.data["video"] = video.id
        request.data["course"] = int(request.data["course"])
        request.data["time"] = get_video_time(str(video.video))

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
    permission_classes = [IsAuthenticatedOrReadOnly, ]

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
