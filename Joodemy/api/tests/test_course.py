from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model

from accounts.models import Instructor
from course.models import Course, Image


class TestCourse(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_instructor", email="test@test.com", password="password", is_instructor=True)
        self.instructor = Instructor.objects.filter(user=self.user)[0]

        self.image = Image.objects.create()

        self.course1 = Course.objects.create(instructor=self.instructor,
                                             title="test course1", description="desciption",
                                             price=19.99, img=self.image)
        self.course2 = Course.objects.create(instructor=self.instructor,
                                             title="test course2", description="desciption",
                                             price=29.99, img=self.image)

        self.client.force_authenticate(user=self.user)

    def test_get_course_list(self):
        """ 강의 리스트 API """

        url = "/api/courses/"

        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_create_course(self):
        """ 강의 생성 API """

        url = "/api/courses/"

        img = open("api/tests/test_image.png", "rb")

        payload = {
            "instructor": self.user.id,
            "title": "test course1",
            "description": "desciption",
            "price": 19.99,
            "img": img
        }

        res = self.client.post(url, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["instructor"], self.instructor.user.username)

    def test_delete_course(self):
        """ 강의 삭제 API """

        url = "/api/courses/"+str(self.course2.id)+"/"

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
