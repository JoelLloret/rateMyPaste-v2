from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *


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


@login_required
def pokemon_list(request):
    pokemons = someonesPokemon.objects.filter(user=request.user)
    return render(request, 'web/pokemon_list.html', {'pokemons': pokemons})


@login_required
def paste_list(request):
    pastes = PokePaste.objects.filter(user=request.user)
    return render(request, 'web/paste_list.html', {'pastes': pastes})


@login_required
def pokemon_create(request):
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


@login_required
def paste_create(request):
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


@login_required
def pokemon_edit(request, pk):
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


@login_required
def paste_edit(request, pk):
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


@login_required
def pokemon_delete(request, pk):
    pokemon = get_object_or_404(someonesPokemon, pk=pk)
    if pokemon.user == request.user:
        pokemon.delete()
    return redirect('pokemon_list')


@login_required
def paste_delete(request, pk):
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
