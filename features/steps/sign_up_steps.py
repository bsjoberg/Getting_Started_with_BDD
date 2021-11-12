from behave import given, when, then


@given(u'I navigated to our online bank website')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I navigated to our online bank website')


@when(u'I submit an application with valid details')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I submit an application with valid details')


@when(u'Select an account type')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Select an account type')


@then(u'I am notified of my account status')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am notified of my account status')
