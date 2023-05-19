from behave import *

use_step_matcher("parse")


@then('I\'m viewing the details for the Paste {name}')
@when('I\'m viewing the details for the Paste {name}')
def step_impl(context, name):
    from web.models import PokePaste
    paste = PokePaste.objects.get(name=name)
    context.browser.visit(context.get_url('paste_detail', paste.pk))


@then('The attribute has been changed to {attribute}')
def step_impl(context, attribute):
    context.browser.is_text_present(attribute)


@then("I'm viewing Paste details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])
