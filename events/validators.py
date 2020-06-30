import datetime
from django.forms import ValidationError


def is_valid_event_date(date):
    """Check if future date."""
    if date <= datetime.date.today():
        raise ValidationError('You cannot create event in the past')
    return date

# flake8: noqa DAR201
