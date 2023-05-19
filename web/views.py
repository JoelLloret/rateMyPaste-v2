import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *
from django.core.serializers import serialize
from django.http import HttpResponse


def home(request):
    return render(request, 'web/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserCreationForm

    context = {'form': form}
    return render(request, 'web/register.html', context)


def pokemon_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    pokemons = someonesPokemon.objects.filter(user=request.user)
    return render(request, 'web/pokemon_list.html', {'pokemons': pokemons})


def paste_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    pastes = PokePaste.objects.filter(user=request.user)
    return render(request, 'web/paste_list.html', {'pastes': pastes})


def pokemon_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.user = request.user
            pokemon.save()
            return redirect('pokemon_list')
    else:
        form = PokemonForm()
    return render(request, 'web/pokemon_form.html', {'form': form})


def paste_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = PasteForm(request.user, request.POST)
        if form.is_valid():
            paste = form.save(commit=False)
            paste.user = request.user
            paste.save()
            return redirect('paste_list')
    else:
        form = PasteForm(request.user)
    return render(request, 'web/paste_form.html', {'form': form})


def pokemon_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    pokemon = get_object_or_404(someonesPokemon, pk=pk)
    if pokemon.user != request.user:
        return redirect('pokemon_list')
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.user = request.user
            pokemon.save()
            return redirect('pokemon_list')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'web/pokemon_form.html', {'form': form})


def paste_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    paste = get_object_or_404(PokePaste, pk=pk)
    if paste.user != request.user:
        return redirect('paste_list')
    if request.method == 'POST':
        form = PasteForm(request.user, request.POST, instance=paste)
        if form.is_valid():
            paste = form.save(commit=False)
            paste.user = request.user
            paste.save()
            return redirect('paste_list')
    else:
        form = PasteForm(request.user, instance=paste)
    return render(request, 'web/paste_form.html', {'form': form})


def pokemon_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    pokemon = get_object_or_404(someonesPokemon, pk=pk)
    if pokemon.user == request.user:
        pokemon.delete()
    return redirect('pokemon_list')


def paste_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    paste = get_object_or_404(PokePaste, pk=pk)
    if paste.user == request.user:
        paste.delete()
    return redirect('paste_list')


def pokemon_detail(request, pk):
    pokemon = get_object_or_404(someonesPokemon, pk=pk)
    if pokemon.user != request.user:
        return redirect('pokemon_list')
    return render(request, 'web/pokemon_detail.html', {'pokemon': pokemon})


def paste_detail(request, pk):
    paste = get_object_or_404(PokePaste, pk=pk)
    if paste.user != request.user:
        return redirect('paste_list')
    return render(request, 'web/paste_detail.html', {'paste': paste})


def pokemons(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'GET':
        pokemon_filter = request.GET.get('pokemon_filter', '')
        limit = request.GET.get('limit', '10')
        pokemons = Pokemon.objects.filter(name__istartswith=pokemon_filter)[:int(limit)]
        print(pokemons)
        poke_array = [{'name': p.name, 'img': p.img_url, 'id': p.id} for p in pokemons]
        response_dict = {
            'limit': limit,
            'count': limit,
            'results': poke_array,
        }
        return HttpResponse(json.dumps(response_dict), content_type="application/json")
    else:
        render(request, 'web/logout.html')


"""@login_required
def attacks(request, attck):
    attacks = Attack.objects.filter(name__istartswith=attck)
    return render(request, 'web/pokemon_list.html', {'pokemons': pokemons})


@login_required
def items(request, item):
    items = Item.objects.filter(name__istartswith=item)
    return render(request, 'web/pokemon_list.html', {'pokemons': pokemons})"""
