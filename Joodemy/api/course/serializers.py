from rest_framework import serializers

from course.models import Course, Content, Review


class CourseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("instructor", "title", "description", "price", "img")


class CourseSerializer(CourseCreateSerializer):
    instructor = serializers.StringRelatedField()


class ContentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ("course", "title", "video", "time")


class ContentSerializer(ContentCreateSerializer):

    course = serializers.StringRelatedField()


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("course", "user", "rating", "text")


class ReviewSerializer(ReviewCreateSerializer):

    course = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
