from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=1000, null=True)

    def __str__(self) -> str:
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type1 = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, related_name="type1")
    type2 = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, related_name="type2")
    img_url = models.CharField(max_length=1000, null=True)

    def __str__(self) -> str:
        return self.name


class Attack(models.Model):
    name = models.CharField(max_length=100)
    type1 = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name


class someonesPokemon(models.Model):
    nickname = models.CharField(max_length=100)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    attack1 = models.ForeignKey(Attack, on_delete=models.SET_NULL, null=True, related_name="attack1")
    attack2 = models.ForeignKey(Attack, on_delete=models.SET_NULL, null=True, related_name="attack2")
    attack3 = models.ForeignKey(Attack, on_delete=models.SET_NULL, null=True, related_name="attack3")
    attack4 = models.ForeignKey(Attack, on_delete=models.SET_NULL, null=True, related_name="attack4")
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    tera_type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.nickname + " (" + self.pokemon.name + ")"


class PokePaste(models.Model):
    name = models.CharField(max_length=150)
    pokemon1 = models.ForeignKey(someonesPokemon, on_delete=models.SET_NULL, null=True, related_name="pokemon1")
    pokemon2 = models.ForeignKey(someonesPokemon, on_delete=models.SET_NULL, null=True, related_name="pokemon2")
    pokemon3 = models.ForeignKey(someonesPokemon, on_delete=models.SET_NULL, null=True, related_name="pokemon3")
    pokemon4 = models.ForeignKey(someonesPokemon, on_delete=models.SET_NULL, null=True, related_name="pokemon4")
    pokemon5 = models.ForeignKey(someonesPokemon, on_delete=models.SET_NULL, null=True, related_name="pokemon5")
    pokemon6 = models.ForeignKey(someonesPokemon, on_delete=models.SET_NULL, null=True, related_name="pokemon6")
    pokepaste_code = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name
