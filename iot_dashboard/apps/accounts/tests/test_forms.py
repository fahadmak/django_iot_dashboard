from django.test import TestCase
from ..forms import UserCreateForm


class TestUserForms(TestCase):
    def test_forms(self):
        form_data = {'username': 'Hellosvbsvbcs', "email": "fahad@wesnvsbs.com",
                     "password1": "Manny0900", "password2": "Manny0900"}
        form = UserCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

