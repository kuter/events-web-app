import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse, reverse_lazy

import factory
from factory import Iterator

from participants.factories import UserFactory

from ..factories import EventFactory, EventParticipantFactory
from ..models import Event, EventParticipant
from .test_base import NEXT_WEEK, TODAY, TOMORROW, YESTERDAY


class LoginRequiredMixin:
    def setUp(self):
        self.user = UserFactory.create()
        self.client.force_login(self.user)

    def assertIsLoginRequired(self, response):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url.split('?')[0], reverse('login'))


class EventViewTests(TestCase):
    url = reverse_lazy('events:list')

    @classmethod
    def setUpClass(cls):
        cls.user = UserFactory.create()

    @classmethod
    def tearDownClass(cls):
        get_user_model().objects.all().delete()

    def test_should_return_upcoming_events_first(self):
        yesterday, today, next_week, tommorow = EventFactory.create_batch(
            4,
            date=Iterator([YESTERDAY, TODAY, NEXT_WEEK, TOMORROW]),
            user=self.user,
        )

        response = self.client.get(self.url)

        self.assertQuerysetEqual(
            response.context['event_list'],
            map(repr, [today, tommorow, next_week]),
            ordered=False,
        )

    def test_shoud_not_return_past_events(self):
        EventFactory.create(date=YESTERDAY, user=self.user)

        response = self.client.get(self.url)

        self.assertQuerysetEqual(response.context['event_list'], [])


class SignUpWithdrawCommonMixin(LoginRequiredMixin):
    def test_should_redirect_to_login_page(self):
        self.client.logout()
        url = reverse(self.url_name, args=[123])

        response = self.client.get(url)

        self.assertIsLoginRequired(response)

    def test_should_return_page_not_found_for_non_existing_event(self):
        url = reverse(self.url_name, args=[123])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_should_redirect_to_event_detail_url(self):
        event = EventFactory.create(date=TOMORROW)
        url = reverse(self.url_name, args=[event.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, event.get_absolute_url())


class SignUpTests(SignUpWithdrawCommonMixin, TestCase):

    url_name = 'events:sign-up'

    def test_should_create_EventParticipant_object(self):
        event = EventFactory.create(date=TOMORROW)
        url = reverse(self.url_name, args=[event.pk])

        self.client.get(url)

        self.assertTrue(
            EventParticipant.objects.filter(
                event=event, user=self.user,
            ).exists(),
        )

    def test_should_not_be_able_to_sign_up_to_past_event(self):
        event = EventFactory.create(date=YESTERDAY)
        url = reverse(self.url_name, args=[event.pk])

        self.client.get(url)

        self.assertFalse(
            EventParticipant.objects.filter(
                event=event, user=self.user,
            ).exists(),
        )


class WithdrawTests(SignUpWithdrawCommonMixin, TestCase):

    url_name = 'events:withdraw'

    def test_should_delete_EventParticipant_object(self):
        event_participant = EventParticipantFactory.create(user=self.user)
        url = reverse(self.url_name, args=[event_participant.event.pk])

        self.client.get(url)

        self.assertFalse(
            EventParticipant.objects.filter(
                event=event_participant.event, user=self.user,
            ).exists(),
        )


class EventCreateTests(LoginRequiredMixin, TestCase):

    url = reverse_lazy('events:create')

    def test_should_redirect_to_login_page(self):
        self.client.logout()

        response = self.client.post(self.url, {})

        self.assertIsLoginRequired(response)

    def test_method_should_set_current_user_as_event_owner(self):
        payload = factory.build(dict, FACTORY_CLASS=EventFactory, user='', date=TOMORROW)

        response = self.client.post(self.url, payload)
        event = Event.objects.get(**resolve(response.url).kwargs)

        self.assertEqual(event.user, self.user)

    def test_should_not_allowed_event_in_the_past(self):
        payload = factory.build(
            dict, FACTORY_CLASS=EventFactory, date=YESTERDAY
        )

        response = self.client.post(self.url, payload)

        self.assertFalse(response.context['form'].is_valid())


class EventDetailTests(LoginRequiredMixin, TestCase):
    url_name = 'events:detail'

    def setUp(self):
        super().setUp()
        self.event = EventFactory.create()
        self.url = reverse(self.url_name, args=[self.event.pk])

    def test_is_particiapte_should_be_false_for_anonymous_user(self):
        self.client.logout()

        response = self.client.get(self.url)

        self.assertFalse(response.context_data['is_user_participate'])

    def test_is_participate_should_be_false(self):
        response = self.client.get(self.url)

        self.assertFalse(response.context_data['is_user_participate'])

    def test_is_participate_should_be_True(self):
        EventParticipantFactory.create(event=self.event, user=self.user)

        response = self.client.get(self.url)

        self.assertTrue(response.context_data['is_user_participate'])


class EventUpdateTests(LoginRequiredMixin, TestCase):
    url_name = 'events:update'

    def test_should_redirect_to_login_page(self):
        self.client.logout()
        url = reverse(self.url_name, args=[123])

        response = self.client.post(url)

        self.assertIsLoginRequired(response)

    def test_logged_user_cannot_update_someone_else_events(self):
        event = EventFactory.create()
        url = reverse(self.url_name, args=[event.pk])
        payload = factory.build(dict, FACTORY_CLASS=EventFactory, user='')

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, 403)

    def test_logged_user_can_edit_own_events(self):
        event = EventFactory.create(user=self.user)
        url = reverse(self.url_name, args=[event.pk])
        payload = {'title': 'foo', 'description': 'bar', 'date': '2000-01-01'}

        response = self.client.post(url, payload, follow=True)
        event.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(event.title, 'foo')
        self.assertEqual(event.description, 'bar')
        self.assertEqual(event.date, datetime.date(2000, 1, 1))
