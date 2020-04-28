from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, username, password=None, is_instructor=False):

        if not email:
            raise ValueError('must have user email')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            is_instructor=is_instructor
        )
        user.set_password(password)
        user.save(using=self._db)

        if is_instructor:
            Instructor.objects.create(user=user)
        else:
            Student.objects.create(user=user)

        return user

    def create_superuser(self, email, username, password):

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student")

    courses = models.ManyToManyField("course.Course", related_name="students")

    def __str__(self):
        return self.user.username


class Instructor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="instructor")

    introduction = models.TextField()

    def __str__(self):
        return self.user.username
