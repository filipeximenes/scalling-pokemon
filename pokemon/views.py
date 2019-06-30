from django.shortcuts import render

from pokemon.models import Pokemon


def pokemon_list(request):
    pokemons = Pokemon.objects.all()

    return render(
        request,
        'pokemon_list.html',
        context={
            'pokemons': pokemons,
        })
