
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom manager for the email-based User model.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular user using email and password.
        """
        if not email:
            raise ValueError("Email address is required.")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
