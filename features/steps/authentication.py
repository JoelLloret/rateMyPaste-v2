from behave import *

use_step_matcher("parse")


@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, password=password)


@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/login/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_text('Login').first.click()
    assert context.browser.is_text_present('Logout')


@given('I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('logout'))
    assert context.browser.is_text_present('Login')


@then('Server responds with page containing "{message}"')
def step_impl(context, message):
    assert context.browser.is_text_present(message)


@then("I'm redirected to the login form")
def step_impl(context):
    assert context.browser.url.startswith(context.get_url('login'))
