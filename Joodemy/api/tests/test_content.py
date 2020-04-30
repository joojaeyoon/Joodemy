from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model

from accounts.models import Instructor
from course.models import Course, Content, Image, Video


class TestContent(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_instructor", email="test@test.com", password="password", is_instructor=True)
        self.instructor = Instructor.objects.filter(user=self.user)[0]

        self.image = Image.objects.create()
        self.video = Video.objects.create()

        self.course = Course.objects.create(instructor=self.instructor,
                                            title="test course1", description="desciption",
                                            price=19.99, img=self.image)

        self.content1 = Content.objects.create(
            course=self.course, title="content1", video=self.video, time="00:24")
        self.content2 = Content.objects.create(
            course=self.course, title="content2", video=self.video, time="00:24")

        self.client.force_authenticate(user=self.user)

    def test_get_content_list(self):
        """ 강의 컨텐츠 리스트 API 테스트 """

        url = "/api/contents/"

        payload = {
            "course_id": self.course.id
        }

        res = self.client.get(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_create_content(self):
        """ 강의 컨텐츠 생성 API 테스트 """

        url = "/api/contents/"

        video = open("api/tests/test.mp4", "rb")

        payload = {
            "course": self.course.id, "title": "test_content",
            "video": video, "time": "14:24"
        }

        res = self.client.post(url, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["title"], "test_content")
        self.assertEqual(res.data["course"], self.course.title)
