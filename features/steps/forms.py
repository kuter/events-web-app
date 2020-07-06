from behave import when


@when('fill {name} input with {value}')
def step_fill_input_by_name_with_value(context, name, value):
    context.browser.fill(name, value)


@when(u'fill {name} text field with "{text}"')
def step_fill_textarea(context, name, text):
    snippet = f"""document.querySelector("textarea[name='{name}']").value = '{text}';"""
    context.browser.execute_script(snippet)


@when(u'fill {name} date field with {value}')
def step_impl(context, name, value):
    snippet = f"""document.querySelector("input[type='date'][name='{name}']").value = '{value}';"""
    context.browser.execute_script(snippet)
