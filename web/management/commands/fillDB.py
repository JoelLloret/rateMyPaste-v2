from ...models import *
from django.core.management.base import BaseCommand
import requests
MAX_LIMIT = 200000


class Command(BaseCommand):
    help = 'Command that populates the DB'
    def _populateDB(self):
        #First we fill our Pokemon models in DB by using the pokeapiv2 +info: https://pokeapi.co/docs/v2

        allTypesURL = "https://pokeapi.co/api/v2/type/"
        params = {'offset':0,'limit':MAX_LIMIT}
        response =  requests.get(allTypesURL,params=params)
        json =  response.json()
        #Plenem el model dels tipos
        for pokeType in json['results']:
            name = pokeType['name']
            if not Type.objects.filter(name="name").exists():
                #Creem els tipos amb id corresponent al seu nom
                modelType = Type(name= name)
                modelType.save()

        #Plenem els models Pokemons
        allPokemonURL = "https://pokeapi.co/api/v2/pokemon/"
        params = {'offset':0,'limit':MAX_LIMIT}
        response =  requests.get(allPokemonURL,params=params)
        json =  response.json()
        for pokemon in json['results']:
            name = pokemon['name']
            if not Pokemon.objects.filter(name=name):
                pokeURL = pokemon['url']
                pokeResponse = requests.get(pokeURL).json()
                type1List = Type.objects.filter(name = pokeResponse['types'][0]['type']['name'])
                type2List = Type.objects.filter(name = pokeResponse['types'][1]['type']['name'] if len(pokeResponse['types'])==2 else "")
                type1 = type1List[0] if len(type1List) == 1 else None
                type2 = type2List[0] if len(type2List) == 1 else None
                sprite = pokeResponse['sprites']['other']['official-artwork']['front_default']
                
                #Creeem els pokemons
                modelPokemon = Pokemon(name=name,type1=type1,type2=type2,img_url=sprite)
                modelPokemon.save()

        #Creeem els items
        itemsURL = "https://pokeapi.co/api/v2/item/"
        params = {'offset':0,'limit':MAX_LIMIT}
        response =  requests.get(itemsURL,params=params)
        json =  response.json()
        for item in json['results']:
            name = item['name']
            if not Item.objects.filter(name=name).exists():
                itemURL = item['url']
                itemResponse = requests.get(itemURL).json()
                sprite = itemResponse['sprites']['default']
                #Creeem els items
                modelItem = Item(name=name,img_url=sprite)
                modelItem.save()
        
        #Creem els attacks
        attacksURL = "https://pokeapi.co/api/v2/move/"
        params = {'offset':0,'limit':MAX_LIMIT}
        response =  requests.get(attacksURL,params=params)
        json =  response.json()
        for attack in json['results']:
            name = attack['name']
            if not Attack.objects.filter(name=name):
                attackURL = attack['url']
                attackInfo =  requests.get(attackURL,params=params).json()
                type1List = Type.objects.filter(name=attackInfo['type']['name'])
                type1 = type1List[0] if len(type1List) == 1 else None
                #Creeem els items
                modelAttack = Attack(name=name,type1=type1)
                modelAttack.save()
        
    def handle(self, *args, **options) :
        self._populateDB()
    