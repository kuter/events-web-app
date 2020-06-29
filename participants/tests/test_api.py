from unittest import skip

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core import mail
from django.test import TestCase

from rest_framework.reverse import reverse_lazy
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient

from events.factories import UserFactory


class SignUpApiViewTests(TestCase):

    url = reverse_lazy('register-list')

    def setUp(self):
        self.client = APIClient()

    def test_should_create_user(self):
        FOO_EMAIL = 'foo@b.ar'
        payload = {
            'email': FOO_EMAIL,
            'password': 's3c43t!Pa$$',
        }

        self.client.post(self.url, payload)

        self.assertTrue(
            get_user_model().objects.filter(email=FOO_EMAIL).exists()
        )

    @skip('send email after API register')
    def test_should_send_email_with_confirmation_link(self):
        payload = {
            'email': 'ab@cd.ef',
            'password': 's3c43t!Pa$$',
        }

        self.client.post(self.url, payload)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Confirm your email')


class LoginApiViewTests(TestCase):

    url = reverse_lazy('token-obtain-pair')

    def setUp(self):
        self.client = APIClient()

    def test_should_return_token_on_successful_login(self):
        PASSWORD = 'test'
        user = UserFactory.create(is_active=True, password=make_password(PASSWORD))

        payload = {
            'email': user.email,
            'password': PASSWORD,
        }

        response = self.client.post(self.url, payload)

        self.assertEqual(response.status_code, HTTP_200_OK)
