from splinter.browser import Browser
from web.models import *


def before_all(context):
    context.browser = Browser('chrome', headless=False)
    attack = Attack(name="pound")
    attack.save()
    item = Item(name="master-ball")
    item.save()
    tera = Type(name="normal")
    tera.save()
    pokemon = Pokemon(name="bulbasaur", type1=tera, type2=tera, img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png")
    pokemon.save()
    attack = Attack(name="cut")
    attack.save()


def after_all(context):
    context.browser.quit()
    context.browser = None
