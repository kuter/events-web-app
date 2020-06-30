import datetime
from django.forms import ValidationError


def is_valid_event_date(date):
    if date <= datetime.date.today():
        raise ValidationError('You cannot create event in the past')
    return date

