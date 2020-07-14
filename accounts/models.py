from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    """Custom user model with email as a username."""

    username = models.CharField(
        _('username'), max_length=50, blank=True, null=True,
    )
    email = models.EmailField(_('email'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        """Canonical URL for an object."""  # noqa: DAR201
        return reverse('profile')
