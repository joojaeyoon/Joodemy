from rest_framework import serializers

from course.models import Course, Content, Review


# Content Serializers
class ContentCreateSerializer(serializers.ModelSerializer):
    """ 컨텐츠 생성 시리얼라이저 """
    class Meta:
        model = Content
        fields = ("course", "title", "video", "time")


class ContentSerializer(ContentCreateSerializer):
    """ 컨텐츠 기본 시리얼라이저 """
    course = serializers.StringRelatedField()
    video = serializers.StringRelatedField()


# Course Serializers
class CourseCreateSerializer(serializers.ModelSerializer):
    """ 강의 생성 시리얼라이저 """

    class Meta:
        model = Course
        fields = ("id", "instructor", "title", "description", "price", "img")


class CourseSerializer(serializers.ModelSerializer):
    """ 강의 기본 시리얼라이저 """

    instructor = serializers.StringRelatedField()
    img = serializers.StringRelatedField()

    class Meta:
        model = Course
        fields = ("id", "instructor", "title",
                  "description", "price", "img")


class CourseRetrieveSerializer(serializers.ModelSerializer):
    """ 강의 디테일 시리얼라이저 """

    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ("id", "instructor", "title",
                  "description", "price", "img", "contents")


# Review Serializers
class ReviewCreateSerializer(serializers.ModelSerializer):
    """ 리뷰 생성 시리얼라이저 """
    class Meta:
        model = Review
        fields = ("course", "user", "rating", "text")


class ReviewSerializer(ReviewCreateSerializer):
    """ 리뷰 기본 시리얼라이저 """

    course = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
