import factory

from django.test import TestCase
from rest_framework.test import APIClient
from ..factories import UserFactory,EventFactory
from rest_framework.reverse import reverse_lazy
from .test_base import TODAY, YESTERDAY, TOMORROW, NEXT_WEEK
from rest_framework.status import HTTP_400_BAD_REQUEST


class EventViewSetTests(TestCase):

    url = reverse_lazy('event-list')

    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory.create()
        self.client.force_login(self.user)

    def test_should_not_allow_to_create_event_in_the_past(self):
        payload = factory.build(dict, FACTORY_CLASS=EventFactory, user='', date=YESTERDAY)

        response = self.client.post(self.url, payload)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
