from django.db import models
from django.utils import timezone


class EventManager(models.Manager):
    """Custom manager for Event objects."""

    def get_queryset(self):  # noqa: D102
        return super().get_queryset().annotate(
            num_participants=models.Count('eventparticipant'),
        ).select_related('user')

    def incoming(self):  # noqa: D102
        return self.get_queryset().filter(
            date__gte=timezone.now(),
        )
