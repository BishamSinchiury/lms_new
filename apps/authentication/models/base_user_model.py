
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager



class UserRole(models.TextChoices):
    """
    Available user roles in the LMS.
    """
    ADMIN = "ADMIN", "Admin"
    TEACHER = "TEACHER", "Teacher"
    STUDENT = "STUDENT", "Student"

class User(AbstractBaseUser):
    """
    Base user model for the application.
    Authentication is performed using email and password.
    """
    email = models.EmailField(
        unique=True,
        db_index=True,
    )
    role = models.CharField(
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.STUDENT,
    )
    # Custom manager
    objects = UserManager()
    # Authentication configuration
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
