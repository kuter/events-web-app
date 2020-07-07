from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import EventManager


def get_sentinel_user():
    """Get or create deleted user.

    Returns:
        User: dummy user

    """
    return get_user_model().objects.get_or_create(
        username='deleted', email='deleted@foo.bar',
    )[0]


class Event(models.Model):
    """Event documentation."""

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'))
    date = models.DateField(_('date'))
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')

    objects = EventManager()

    def __str__(self):
        """Whenever you call str() on an object.

        Returns:
            str: string representation

        """
        return self.title

    def get_absolute_url(self):
        """Event detail url."""  # noqa: DAR201
        return reverse('events:detail', args=[self.pk])

    def get_owner(self):
        """Local part of the email.

        Returns:
            str: event owner

        """
        return self.user.email.split('@')[0]

    def get_amount_of_participants(self):
        """Event participants count."""  # noqa: DAR201
        return self.eventparticipant_set.count()


class EventParticipant(models.Model):
    """Event participant."""

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = [['event', 'user']]
