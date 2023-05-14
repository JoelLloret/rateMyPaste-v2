from django import forms
from .models import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import User


class PokemonForm(forms.ModelForm):
    class Meta:
        model = someonesPokemon
        fields = ['nickname', 'pokemon', 'attack1', 'attack2', 'attack3', 'attack4', 'item', 'tera_type']
        widgets = {'pokemon': forms.CharField()}


class PasteForm(forms.ModelForm):
    class Meta:
        model = PokePaste
        fields = ['name', 'pokemon1', 'pokemon2', 'pokemon3', 'pokemon4', 'pokemon5', 'pokemon6', 'pokepaste_code']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pokemon1'].queryset = someonesPokemon.objects.filter(user=user)
        self.fields['pokemon2'].queryset = someonesPokemon.objects.filter(user=user)
        self.fields['pokemon3'].queryset = someonesPokemon.objects.filter(user=user)
        self.fields['pokemon4'].queryset = someonesPokemon.objects.filter(user=user)
        self.fields['pokemon5'].queryset = someonesPokemon.objects.filter(user=user)
        self.fields['pokemon6'].queryset = someonesPokemon.objects.filter(user=user)
