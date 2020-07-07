import datetime

from django.db import models


class EventManager(models.Manager):
    """Custom manager for Event objects."""

    def incoming(self):  # noqa: D102
        return super().get_queryset().prefetch_related(
            'eventparticipant_set'
        ).filter(
            date__gte=datetime.date.today(),
        ).order_by(
            'date',
        )
