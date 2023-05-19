import time
from functools import reduce
from django.contrib.auth.models import User
from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")


@given('Exists Paste registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from web.models import PokePaste, someonesPokemon
    for row in context.table:
        paste = PokePaste(user=user, name=row[0], pokemon1=someonesPokemon.objects.get(nickname=row[1]), pokemon2=someonesPokemon.objects.get(nickname=row[2]), pokemon3=someonesPokemon.objects.get(nickname=row[3]), pokemon4=someonesPokemon.objects.get(nickname=row[4]), pokemon5=someonesPokemon.objects.get(nickname=row[5]), pokepaste_code=row[7])
        paste.save()


@when('I register Paste')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('paste_create'))
        if context.browser.url == context.get_url('paste_create'):
            context.browser.fill(row.headings[0], row[0])
            for heading in row.headings[1:-1]:
                dropdown = context.browser.find_by_xpath("//select[@name='" + heading + "']")
                option_name = row[heading]+" (bulbasaur)"
                option_xpath = f"//select[@name='" + heading + "']/option[text()='" + option_name + "']"
                option = dropdown.find_by_xpath(option_xpath)
                option.click()
            context.browser.fill('pokepaste_code', row[-1])


@then('There are {count:n} Pastes by {username}')
def step_impl(context, count, username):
    user = User.objects.get(username=username)
    from web.models import PokePaste
    assert count == PokePaste.objects.filter(user=user).count()


@then('I\'m viewing the list of all Pastes of "{username}"')
def step_impl(context, username):
    from web.models import PokePaste
    user = User.objects.get(username=username)
    user_pastes = PokePaste.objects.filter(user=user)

    for paste in user_pastes:
        assert context.browser.is_text_present(paste.name)


@when('I edit the Paste with name "{name}"')
def step_impl(context, name):
    from web.models import PokePaste
    paste = PokePaste.objects.get(name=name)
    for row in context.table:
        context.browser.visit(context.get_url('paste_edit', paste.pk))
        if context.browser.url == context.get_url('paste_edit', paste.pk) \
                and context.browser.find_by_tag('form'):
            context.browser.fill(row.headings[0], row[0])
            for heading in row.headings[1:-2]:
                dropdown = context.browser.find_by_xpath("//select[@name='" + heading + "']")
                option_name = row[heading] + " (bulbasaur)"
                option_xpath = f"//select[@name='" + heading + "']/option[text()='" + option_name + "']"
                option = dropdown.find_by_xpath(option_xpath)
                option.click()
            context.browser.fill('pokepaste_code', row[-1])