from behave import given, then
from django.core import mail
from django.contrib.auth import get_user_model

User = get_user_model()


@given('registered user {email} with password {password}')
def step_given_user(context, email, password):
    get_user_model().objects.create_user(email=email, password=password)


@then('{active} user {email} should be created')
def step_user_exists(context, active, email):
    is_active = True if active == 'active' else False
    assert get_user_model().objects.filter(is_active=is_active, email=email).exists() is True


@then('confirmation link should be sent')
def step_impl(context):
    assert len(mail.outbox) > 0
