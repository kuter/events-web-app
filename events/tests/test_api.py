import factory
from rest_framework.reverse import reverse_lazy
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.test import APITestCase

from accounts.factories import UserFactory

from ..factories import EventFactory
from .test_base import NEXT_WEEK, TODAY, TOMORROW, YESTERDAY


class EventViewSetTests(APITestCase):

    url = reverse_lazy('event-list')

    def setUp(self):
        self.user = UserFactory.create()
        self.client.force_login(self.user)

    def test_should_not_allow_to_create_event_in_the_past(self):
        payload = factory.build(dict, FACTORY_CLASS=EventFactory, user='', date=YESTERDAY)

        response = self.client.post(self.url, payload)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
