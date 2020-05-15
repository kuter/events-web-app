from django.test import TestCase

from ..models import User


class UserManagerTests(TestCase):

    def test_method_raises_exception(self):
        with self.assertRaisesRegex(ValueError, 'The given email must be set'):
            User.objects.create_user(username='test', email=None, password='')

    def test_method_raises_exception_super_user_must_have_staff_true(self):
        extra_fields = {'is_staff': False}
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='test', email=None, password='', **extra_fields,
            )

    def test_method_raises_exception_super_user_must_have_is_superuser_true(self):
        extra_fields = {'is_superuser': False}
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='test', email=None, password='', **extra_fields,
            )

    def test_should_create_super_user_with_empty_username_attr(self):
        user = User.objects.create_superuser(email='foo@b.ar', password='test')

        self.assertTrue(user.is_superuser)
