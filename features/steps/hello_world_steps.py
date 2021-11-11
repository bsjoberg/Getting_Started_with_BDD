from behave import given, when, then

from hello_world import HelloWorld


@given(u'I have a hello_world application')
def step_impl(context):
    assert HelloWorld() is not None


@when(u'I say hi')
def step_impl(context):
    greeter = HelloWorld()
    context.result = greeter.say_hi()


@then(u'I hear "{expected_result}"')
def step_impl(context, expected_result):
    assert expected_result == context.result, 'Expect {} but got {}'.format(expected_result, context.result)
