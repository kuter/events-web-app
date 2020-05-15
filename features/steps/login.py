from django.contrib.auth import get_user_model
from django.urls import reverse

from behave import given, then


@then('I should see I\'m logged in as {email}')
def step_should_see_register_user(context, email):
    assert context.browser.is_element_present_by_text(email) is True


@given('I\'m logged in')
def step_im_logged_in(context):
    get_user_model().objects.create_user(email='test@foo.bar', password='test')
    context.browser.visit(context.get_url(reverse('login')))
    context.browser.fill('username', 'test@foo.bar')
    context.browser.fill('password', 'test')
    button = context.browser.find_by_xpath(
        '//*[@type="submit" and text()="Login"]'
    )
    button.click()
