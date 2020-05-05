from rest_framework import serializers

from accounts.models import User, Student, Instructor


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "is_instructor")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        password = validated_data.pop("password")
        user = User.objects.create_user(**validated_data)

        return user


class StudentSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "courses")
