from django.test import TestCase
from django.urls import reverse

from iot_dashboard.apps.accounts.models import User


class LoginViewTest(TestCase):
    fixtures = ['iot_dashboard/apps/accounts/tests/fixtures/user', ]

    def setUp(self):
        self.credentials = {
            'display_name': 'testuser',
            'email': 'testuser',
            'username': 'testuser',
            'password': 'secret'}
        self.user = User.objects.create_user(**self.credentials)

    def test_login_user(self):

        # send login data
        response = self.client.post('/accounts/login/', self.credentials)
        # should be logged in now
        self.assertRedirects(response, reverse('dashboard:home'))

    def test_logout_user(self):

        # send login data
        response = self.client.post('/accounts/login/', self.credentials)

        # should be logged out now
        response2 = self.client.get('/accounts/logout/', self.credentials)

        # should be logged in now
        self.assertEqual(response2.status_code, 302)
