from django.test import TestCase

from participants.factories import UserFactory

from ..factories import EventFactory, EventParticipantFactory
from ..models import get_sentinel_user


class EventTests(TestCase):

    def test_should_return_event_owner(self):
        user = UserFactory.create(email='owner@bar.foo')
        event = EventFactory.create(user=user)

        rv = event.get_owner()

        self.assertEqual(rv, 'owner')

    def test_get_sentinel_user_should_return_user_with_username_deleted(self):
        rv = get_sentinel_user()

        self.assertEqual(rv.username, 'deleted')

    def test_should_return_amount_of_participants(self):
        AMOUNT = 3
        event = EventFactory.create()
        EventParticipantFactory.create_batch(AMOUNT, event=event)

        rv = event.get_amount_of_participants()

        self.assertEqual(rv, AMOUNT)
