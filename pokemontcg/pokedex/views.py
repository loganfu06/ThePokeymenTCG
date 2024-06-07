from django.shortcuts import render, redirect

import json
import http.client
import requests
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Pokemon, Type, Trainer, Energy, PokemonNames
from django.views.generic import ListView
# Create your views here.

class PokemonListView(ListView):
    model = Pokemon

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemon_names'] = PokemonNames.objects.all()
        return context
    
def loadInitialData(request):
    if Type.objects.count() > 0:

        # Add code for message about initial data already loaded
        messages.add_message(
            request, messages.SUCCESS,
            'Types already loaded.'
        )

        print("Type data already loaded")
        return redirect('pokedex:home')
    else:
        api_url = 'https://api.pokemontcg.io/v2/types'
        response = requests.get(api_url)
        types = response.json()
        # print(types['data'])
        for type_name in types['data']:
            print(type_name)
            current_type = Type(
                name = type_name
            )
            current_type.save()

        # Add some cards into the database
        insertInitialCards()
        
        # Add code for message about initial data successfully loading
        messages.add_message(
            request, messages.SUCCESS,
            'Successfully loaded all Types.'
        )

        # print("Type data successfully loaded")
        return redirect('pokedex:home')
    
def insertInitialCards():
    api_url = 'https://api.pokemontcg.io/v2/cards?q=set.id:base1'
    response = requests.get(api_url)
    set_data = response.json()['data']
    for card_data in set_data:
        try:
            if card_data['supertype'] == 'Pokémon':
                conditions = card_data['tcgplayer']['prices']
                highest_market = 0
                for condition in conditions:
                    current_market = card_data['tcgplayer']['prices'][condition]['market']
                    if current_market > highest_market:
                        highest_market = current_market

                current_pokemon = Pokemon(
                    card_id = card_data['id'],
                    name = card_data['name'],
                    rarity = card_data['rarity'],
                    image = card_data['images']['large'],
                    prices = card_data['tcgplayer'],
                    highest_market_price = highest_market,
                )
                current_pokemon.save()

                for type in card_data['types']:
                    current_type = Type.objects.get(name=type)
                    current_pokemon.types.add(current_type)
                current_pokemon.save()

            # Add trainer card data
            elif card_data['supertype'] == 'Trainer':
                conditions = card_data['tcgplayer']['prices']
                highest_market = 0
                for condition in conditions:
                    current_market = card_data['tcgplayer']['prices'][condition]['market']
                    if current_market > highest_market:
                        highest_market = current_market

                current_trainer = Trainer(
                    card_id = card_data['id'],
                    name = card_data['name'],
                    rarity = card_data['rarity'],
                    image = card_data['images']['large'],
                    prices = card_data['tcgplayer'],
                    highest_market_price = highest_market,
                )
                current_trainer.save()
            
            # Add energy card data
            elif card_data['supertype'] == 'Energy':      
                conditions = card_data['tcgplayer']['prices']
                highest_market = 0
                for condition in conditions:
                    current_market = card_data['tcgplayer']['prices'][condition]['market']
                    if current_market > highest_market:
                        highest_market = current_market

                current_energy = Energy(
                    card_id = card_data['id'],
                    name = card_data['name'],
                    image = card_data['images']['large'],
                    prices = card_data['tcgplayer'],
                    highest_market_price = highest_market,
                )
                current_energy.save()
        except KeyError:
            # Add message about missing key from API (NOT MY FAULT BRO)
            print("This card is missing data from API")

def createPokemonCard(request, card_id):
    if Type.objects.count() == 0:
        # Add code for error message about needing to load initial data first
        print("Please load initial data")
        return redirect('pokedex:test')

    api_url = 'https://api.pokemontcg.io/v2/cards/{f_cardID}'.format(f_cardID = card_id)
    response = requests.get(api_url)

    if response.status_code == 200:
        card_data = response.json()['data']
        try:
            # Add pokemon type card
            if card_data['supertype'] == 'Pokémon':
                if Pokemon.objects.filter(card_id=card_data['id']).exists():
                    # Add code for error message about card already existing
                    print("Pokemon card already exists")
                    return redirect('pokedex:test')
                
                conditions = card_data['tcgplayer']['prices']
                highest_market = 0
                for condition in conditions:
                    current_market = card_data['tcgplayer']['prices'][condition]['market']
                    if current_market > highest_market:
                        highest_market = current_market

                current_pokemon = Pokemon(
                    card_id = card_data['id'],
                    name = card_data['name'],
                    rarity = card_data['rarity'],
                    image = card_data['images']['large'],
                    prices = card_data['tcgplayer'],
                    highest_market_price = highest_market,
                )
                current_pokemon.save()

                for type in card_data['types']:
                    current_type = Type.objects.get(name=type)
                    current_pokemon.types.add(current_type)
                current_pokemon.save()

            # Add trainer card data
            elif card_data['supertype'] == 'Trainer':
                if Trainer.objects.filter(card_id=card_data['id']).exists():
                    # Add code for error message about card already existing
                    print("Pokemon card already exists")
                    return redirect('pokedex:test')
                
                conditions = card_data['tcgplayer']['prices']
                highest_market = 0
                for condition in conditions:
                    current_market = card_data['tcgplayer']['prices'][condition]['market']
                    if current_market > highest_market:
                        highest_market = current_market

                current_trainer = Trainer(
                    card_id = card_data['id'],
                    name = card_data['name'],
                    rarity = card_data['rarity'],
                    image = card_data['images']['large'],
                    prices = card_data['tcgplayer'],
                    highest_market_price = highest_market,
                )
                current_trainer.save()
            
            # Add energy card data
            elif card_data['supertype'] == 'Energy':
                if Energy.objects.filter(card_id=card_data['id']).exists():
                    # Add code for error message about card already existing
                    print("Pokemon card already exists")
                    return redirect('pokedex:test')
                
                conditions = card_data['tcgplayer']['prices']
                highest_market = 0
                for condition in conditions:
                    current_market = card_data['tcgplayer']['prices'][condition]['market']
                    if current_market > highest_market:
                        highest_market = current_market

                current_energy = Energy(
                    card_id = card_data['id'],
                    name = card_data['name'],
                    image = card_data['images']['large'],
                    prices = card_data['tcgplayer'],
                    highest_market_price = highest_market,
                )
                current_energy.save()
        except KeyError:
            # Add message about missing key from API (NOT MY FAULT BRO)
            print("This card is missing data from API")




        # print(card_data)
        messages.add_message(
            request, messages.SUCCESS,
            'added ' + card_data['name'] + '.'
        )

    return redirect('pokedex:test')

def testView(request):
    return render(request, 'pokedex/test.html')

def homeView(request):
    return render(request, 'pokedex/home.html')
def detailView(request):
    return redner(request, 'pokedex/detailView.html')