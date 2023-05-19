from functools import reduce
from django.contrib.auth.models import User
from behave import *
import operator
from django.db.models import Q
import time
from web.models import *

use_step_matcher("parse")


@given('Exists Pokémon registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    for row in context.table:
        pokemon = someonesPokemon(user=user, pokemon=Pokemon.objects.get(name=row[1]), nickname=row[0], attack1=Attack.objects.get(name=row[2]), attack2=Attack.objects.get(name=row[3]), attack3=Attack.objects.get(name=row[4]), attack4=Attack.objects.get(name=row[5]), item=Item.objects.get(name=row[6]))
        pokemon.save()


@when('I register Pokémon')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('pokemon_create'))
        if context.browser.url == context.get_url('pokemon_create'):
            context.browser.fill('pokemon_searcher', row[0])
            context.browser.find_by_text(row[0]).first.click()
            context.browser.fill('nickname', row[1])
            for heading in row.headings[2:-1]:
                dropdown = context.browser.find_by_xpath("//select[@name='"+heading+"']")
                option_name = row[heading]
                option_xpath = f"//select[@name='"+heading+"']/option[text()='"+option_name+"']"
                option = dropdown.find_by_xpath(option_xpath)
                option.click()
            dropdown = context.browser.find_by_xpath("//select[@name='tera_type']")
            option_xpath = f"//select[@name='tera_type']/option[text()='normal']"
            option = dropdown.find_by_xpath(option_xpath)
            option.click()
            context.browser.find_by_css('button[type="submit"]').first.click()


@then('There are {count:n} Pokémons by {username}')
def step_impl(context, count, username):
    user = User.objects.get(username=username)
    """assert count == someonesPokemon.objects.filter(user=user).count()"""


@then('I\'m viewing the list of all Pokémons of "{username}"')
def step_impl(context, username):
    user = User.objects.get(username=username)
    user_pokemons = someonesPokemon.objects.filter(user=user)

    for pokemon in user_pokemons:
        assert context.browser.is_text_present(pokemon.nickname)


@when('I edit the Pokémon with name "{name}"')
def step_impl(context, name):
    from web.models import someonesPokemon
    pokemon = someonesPokemon.objects.get(nickname=name)
    context.browser.visit(context.get_url('pokemon_edit', pokemon.pk))
    if context.browser.url == context.get_url('pokemon_edit', pokemon.pk) \
            and context.browser.find_by_tag('form'):
        for row in context.table:
            for heading in row.headings[2:-1]:
                dropdown = context.browser.find_by_xpath("//select[@name='" + heading + "']")
                option_name = row[heading]
                option_xpath = f"//select[@name='" + heading + "']/option[text()='" + option_name + "']"
                option = dropdown.find_by_xpath(option_xpath)
                option.click()
            dropdown = context.browser.find_by_xpath("//select[@name='tera_type']")
            option_xpath = f"//select[@name='tera_type']/option[text()='normal']"
            option = dropdown.find_by_xpath(option_xpath)
            option.click()
            context.browser.find_by_css('button[type="submit"]').first.click()
