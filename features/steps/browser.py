from behave import given, when, then


@given('I see index page')
def step_I_see_page(context):
    context.browser.visit(context.get_url('/'))


@when('fill {name} input with {value}')
def step_fill_input_by_name_with_value(context, name, value):
    context.browser.fill(name, value)


@when('click {text} button')
def step_click_button_by_text(context, text):
    button = context.browser.find_by_xpath(
        f'//*[@type="submit" and text()="{text}"]'
    )
    button.click()


@when('I click on "{text}" menu item')
def step_click_on_the_menu_item(context, text):
    nav_item = context.browser.find_by_xpath(f'//li/a[text()="{text}"]')
    nav_item.click()



@then('I should see "{text}" heading')
def step_h1_with_given_text_is_present(context, text):
    assert context.browser.is_element_present_by_xpath(f'//h1[text()="{text}"]') is True
