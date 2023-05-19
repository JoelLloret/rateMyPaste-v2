import time

from behave import *

use_step_matcher("parse")


@when('I list Pastes')
def step_impl(context):
    context.browser.visit(context.get_url('paste_list'))


@step('The list contains {count:n} Pastes')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('div#content ul li a'))


@then(u'I am viewing a Paste list containing')
def step_impl(context):
    for row in context.table.rows:
        for item in row:
            assert item in context.browser.html, f"{item}"
