from rest_framework.test import APITestCase
from rest_framework import status

from accounts.models import User, Instructor
from course.models import Course, Review


class TestReview(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test_instructor", email="test@test.com", password="password", is_instructor=True
        )
        self.user2 = User.objects.create_user(
            username="review user", email="review@review.com", password="password"
        )
        self.instructor = Instructor.objects.filter(user=self.user)[0]

        self.course = Course.objects.create(instructor=self.instructor,
                                            title="test course1", description="desciption",
                                            price=19.99, img="http://test.jpg")

        self.review1 = Review.objects.create(
            course=self.course, user=self.user2, rating=5, text="Awesome!!"
        )
        self.review1 = Review.objects.create(
            course=self.course, user=self.user2, rating=4, text="Greate Course!"
        )

        self.client.force_authenticate(user=self.user)

    def test_get_review_list(self):
        """ 리뷰 리스트 API 테스트 """

        url = "/api/reviews/"

        payload = {
            "course_id": self.course.id
        }

        res = self.client.get(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_create_review(self):
        """ 리뷰 생성 API 테스트 """

        url = "/api/reviews/"

        payload = {
            "course": self.course.id,
            "user": self.user.id,
            "rating": 5,
            "text": "Just Perfect Course!"
        }

        res = self.client.post(url, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["course"], self.course.title)
        self.assertEqual(res.data["user"], self.user.username)
