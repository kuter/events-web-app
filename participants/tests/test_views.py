from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from events.factories import UserFactory


class LoginRequiredMixin:
    def setUp(self):
        self.user = UserFactory.create()
        self.client.force_login(self.user)

    def assertIsLoginRequired(self, response):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url.split('?')[0], reverse('login'))


class SignUpViewTests(TestCase):
    url = reverse_lazy('signup')
    payload = {
        'email': 'foo@b.ar',
        'password1': 's3c43t!Pa$$',
        'password2': 's3c43t!Pa$$',
    }

    def test_should_create_inactive_user_object(self):
        self.client.post(self.url, self.payload)

        self.assertTrue(
            get_user_model().objects.filter(
                email='foo@b.ar', is_active=False,
            ).exists(),
        )

    def test_should_send_email_with_confirmation_link(self):
        self.client.post(self.url, self.payload)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Confirm your email')

    def test_if_email_body_contains_link(self):
        self.client.post(self.url, self.payload)

        user = get_user_model().objects.get(email='foo@b.ar')
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        expected_url = reverse('email_confirm', args=[uidb64, token])

        self.assertIn(expected_url, mail.outbox[0].body)


class EmailConfirmViewTests(TestCase):
    url_name = 'email_confirm'

    def setUp(self):
        self.user = UserFactory.create(is_active=False)
        self.client.force_login(self.user)

    def test_should_return_404_if_invalid_uuid64(self):
        url = reverse(self.url_name, args=['XXXX', 'a789dfa08fas'])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_should_return_to_index_page_on_invalid_token(self):
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        url = reverse(self.url_name, args=[uidb64, 'a789dfa08fas'])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('events:list'))

    def test_should_set_is_active_true_if_valid_kwargs(self):
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)

        url = reverse(self.url_name, args=[uidb64, token])

        response = self.client.get(url)
        self.user.refresh_from_db()

        self.assertTrue(self.user.is_active)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))


class ProfileViewTests(LoginRequiredMixin, TestCase):
    url_name = 'profile'

    def test_should_redirect_to_login_page(self):
        self.client.logout()

        response = self.client.get(reverse(self.url_name))

        self.assertIsLoginRequired(response)

    def test_should_return_user_profile(self):
        response = self.client.get(reverse(self.url_name))

        self.assertIn(self.user, response.context_data.values())
