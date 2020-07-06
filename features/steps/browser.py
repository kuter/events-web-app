from behave import given, when, then


@given('I see index page')
def step_I_see_page(context):
    context.browser.visit(context.get_url('/'))


@when('click {text} button')
def step_click_button_by_text(context, text):
    button = context.browser.find_by_xpath(
        f'//*[@type="submit" and text()="{text}"]'
    )
    button.click()


@given('I click on "{text}" menu item')
@when('I click on "{text}" menu item')
def step_click_on_the_menu_item(context, text):
    nav_item = context.browser.find_by_xpath(f'//li/a[text()="{text}"]')
    nav_item.click()


@then('I should see "{text}" heading')
def step_h1_with_given_text_is_present(context, text):
    assert context.browser.is_element_present_by_xpath(f'//h1[text()="{text}"]') is True


@given(u'I\'m on create view page')
def step_I_am_on_create_view_page(context):
    context.browser.visit(context.get_url('/create/'))

@then(u'I should see "{text}" error')
def step_I_should_see_error(context, text):
    assert context.browser.is_element_present_by_xpath(f'//ul/li[text()="{text}"]') is True
