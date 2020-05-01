from rest_framework import serializers

from course.models import Course, Content, Review


class ContentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ("course", "title", "video", "time")


class ContentSerializer(ContentCreateSerializer):
    course = serializers.StringRelatedField()
    video = serializers.StringRelatedField()


class CourseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "instructor", "title", "description", "price", "img")


class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField()
    img = serializers.StringRelatedField()

    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ("id", "instructor", "title",
                  "description", "price", "img", "contents")


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("course", "user", "rating", "text")


class ReviewSerializer(ReviewCreateSerializer):

    course = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
