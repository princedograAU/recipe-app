from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""

        email = 'test@test.com'     # test email
        password = 'password@123'   # test password

        # creating the user
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        # check if user is created with the correct email
        self.assertEqual(user.email, email)
        
        # checking password using check_password built-in method because passwords 
        # are stored as hashes in django
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the new user email is normalized"""

        email = 'test@TEST.COM'     # test email
        password = 'password@123'   # test password

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        # check if email is stored as lower case or not
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='password@123'
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            email='admin@admin.com',
            password='password@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)