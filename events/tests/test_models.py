from django.db import IntegrityError
from django.test import TestCase

from accounts.factories import UserFactory

from ..factories import EventFactory, EventParticipantFactory
from ..models import Event, get_sentinel_user
from .test_base import TOMORROW


class EventTests(TestCase):

    def test_should_return_event_owner(self):
        user = UserFactory.create(email='owner@bar.foo')
        EventFactory.create(user=user, date=TOMORROW)

        event = Event.objects.incoming().first()

        self.assertEqual(event.user.get_name(), 'owner')

    def test_get_sentinel_user_should_return_user_with_username_deleted(self):
        rv = get_sentinel_user()

        self.assertEqual(rv.username, 'deleted')

    def test_should_return_amount_of_participants(self):
        AMOUNT = 3
        EventParticipantFactory.create_batch(
            AMOUNT, event=EventFactory.create(date=TOMORROW)
        )

        event = Event.objects.incoming().first()

        self.assertEqual(event.num_participants, AMOUNT)


class EventParticipantTests(TestCase):

    def test_should_not_allow_to_create_duplicate_object(self):
        user = UserFactory.create()
        event = EventFactory.create()

        with self.assertRaises(IntegrityError):
            EventParticipantFactory.create_batch(2, event=event, user=user)
