from django.db import models
from accounts.models import Instructor, User


class Image(models.Model):
    image = models.ImageField()


class Video(models.Model):
    video = models.FileField()


class Course(models.Model):
    instructor = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, related_name="courses")
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.CharField(max_length=12)
    img = models.ForeignKey(Image, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Content(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="contents")
    title = models.CharField(max_length=64)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField()
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
