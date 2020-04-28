from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model


class TestUser(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test",
                                                         email="test@jooz.dev", password="password")
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """ 유저 생성 API 테스트 """

        url = "/api/auth/registration/"

        payload = {
            "username": "test_user",
            "email": "test@gmail.com",
            "password": "supersecret",
            "is_instructor": False
        }

        res = self.client.post(url, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["username"], "test_user")
        self.assertEqual(res.data["email"], "test@gmail.com")

    def test_login_user(self):
        """ 유저 로그인 API 테스트 """

        url = "/api/auth/login/"

        payload = {
            "username": "test",
            "password": "password"
        }

        res = self.client.post(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(res.data["token"])
        self.assertEqual(res.data["user"]["username"], "test")
