from django.test import TestCase

from iot_dashboard.apps.accounts.models import User


class UserModelTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'fahdmak',
            'password': 'yuoirt',
            'display_name': 'display',
            'email': 'email@aol.com'
        }

    def test_user_created(self):
        user = User.objects.create_user(**self.credentials)
        self.assertEquals(str(user), '@' + self.credentials['username'])
        self.assertEquals(user.username, self.credentials['username'])
        self.assertEquals(user.get_short_name(), self.credentials['display_name'])
        self.assertEquals(user.get_long_name(),  f"{self.credentials['display_name']} @({self.credentials['username']})")

    def test_superuser_created(self):
        user = User.objects.create_superuser(**self.credentials)
        self.assertEquals(user.email, self.credentials['email'])
        self.assertTrue(user.is_staff)

    def test_create_user_if_no_username(self):
        """test that user is not created because no username"""
        error_msg = "Username is required"
        with self.assertRaisesMessage(ValueError, error_msg):
            user = User.objects.create_user(display_name='username', email='username@we.com', password='password')

