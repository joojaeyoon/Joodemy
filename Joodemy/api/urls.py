from django.urls import path, include

from rest_framework import routers

from .accounts.views import *
from .course.views import *

router = routers.DefaultRouter()
router.register(r"^", UserRegistrationViewSet)

course_router = routers.DefaultRouter()
course_router.register("courses", CourseViewSet)
course_router.register("contents", ContentViewSet)
course_router.register("reviews", ReviewViewSet)


app_name = "api"

urlpatterns = [
    path("auth/registration", include(router.urls)),
    path("auth/", include("rest_auth.urls")),
    path("", include(course_router.urls)),
]
