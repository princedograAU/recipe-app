from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""

        if not email:
            raise ValueError('User must have an email')

        # create the user with email and add the extra fields to it
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        # password needs to be encrypted
        user.set_password(password)

        # save the user with the help of using to support multiple database
        user.save(using=self._db)

        # return the newly created user
        return user

    def create_superuser(self, email, password):
        """Create and saves a new super user"""

        # create the user with email and password
        user = self.create_user(
            email=email,
            password=password
        )

        # setting user as a staff
        user.is_staff = True

        # setting user as a superuser
        user.is_superuser = True

        # save the user with the help of using to support multiple database
        user.save(using=self._db)

        # return the newly created superuser
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""

    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

