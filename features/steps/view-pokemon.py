from behave import *
from web.models import *
import time
use_step_matcher("parse")


@then('I\'m viewing the details for the Pokémon {name}')
@when('I\'m viewing the details for the Pokémon {name}')
def step_impl(context, name):
    pokemon = someonesPokemon.objects.get(nickname=name[1:-1])
    context.browser.visit(context.get_url('pokemon_detail', pokemon.pk))


@then("I'm viewing Pokémon details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])
