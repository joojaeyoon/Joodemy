from rest_framework import serializers

from course.models import Course, Content, Review


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("instructor", "title", "description", "price", "img")


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ("course", "title", "video", "time")


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ("course", "user", "rating", "text")
