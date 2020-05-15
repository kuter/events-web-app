import datetime

from django.contrib.auth import get_user_model

import factory
from factory.fuzzy import FuzzyDate

from .models import Event, EventParticipant


class UserFactory(factory.DjangoModelFactory):
    """User factory."""

    username = factory.Faker('user_name')
    email = factory.Faker('email')

    class Meta:
        model = get_user_model()


class EventFactory(factory.DjangoModelFactory):
    """DjangoModelFactory for object Event."""

    title = factory.Faker('bs')
    description = factory.Faker('sentence')
    date = FuzzyDate(datetime.date(2020, 1, 1))
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Event


class EventParticipantFactory(factory.DjangoModelFactory):
    """Factory for EventParticipant model."""

    event = factory.SubFactory(EventFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = EventParticipant
