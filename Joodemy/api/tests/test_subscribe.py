from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model

from accounts.models import Instructor, Student
from course.models import Course, Image


class TestSubscribe(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_instructor", email="test@test.com", password="password", is_instructor=True)
        self.instructor = Instructor.objects.filter(user=self.user)[0]

        self.user2 = get_user_model().objects.create_user(
            username="test_student", email="student@gmail.com", password="password"
        )
        self.student = Student.objects.filter(user=self.user2)[0]

        self.image = Image.objects.create()

        self.course1 = Course.objects.create(instructor=self.instructor,
                                             title="test course1", description="desciption",
                                             price=19.99, img=self.image)
        self.course2 = Course.objects.create(instructor=self.instructor,
                                             title="test course2", description="desciption",
                                             price=29.99, img=self.image)

        self.client.force_authenticate(user=self.user)

    def test_subscribe_course(self):
        """ 강의 구독 테스트 """

        payload = {
            "student": self.student.id,
            "course": self.course1.id,
        }

        url = "/api/subscribes/"

        res = self.client.post(url, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_invalid_subscribe(self):
        """ 잘못된 구독 요청 테스트 """

        payload = {
            "student": self.student.id,
            "course": 999,
        }

        url = "/api/subscribes/"

        res = self.client.post(url, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_subscribe_list(self):
        """ 구독 강의 리스트 테스트 """

        payload = {
            "student": self.student.id
        }

        url = "/api/subscribes/"

        res = self.client.get(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(res.data["courses"])
