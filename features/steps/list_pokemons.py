import time

from behave import *

use_step_matcher("parse")


@when('I list Pokémons')
def step_impl(context):
    context.browser.visit(context.get_url('pokemon_list'))


@step('The list contains {count:n} Pokémons')
def step_impl(context, count):
    l = len(context.browser.find_by_tag('a'))
    assert count + 3 == l, f"{l}"


@then("I'm viewing a list of Pokémons containing")
def step_impl(context):
    for row in context.table.rows:
        displayed_pokemons = context.browser.find_by_tag('a').text.split('\n')
        for item in row:
            assert item in displayed_pokemons
