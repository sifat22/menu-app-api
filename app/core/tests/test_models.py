from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    # create email
    def test_create_user_with_email_successfull(self):
        "creating a new user with an email is successfull"
        email = 'tousif2018ahamid@gmail.com'
        password = 'sifat47530'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    # normalize email

    def test_new_user_email_normalized(self):
        "test the email for new user is normalized"
        email = 'tousif2018ahamid@gmail.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    # validation email if email field is blank
    def test_new_user_invalid_email(self):
        "test creating user with no email raise error"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    # create super user
    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
