from django.shortcuts import render, redirect
import os
import json
import pandas as pd
import psycopg as pg
import matplotlib.pyplot as plt 
import numpy as np
import io
import urllib, base64
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# JSON-based secrets module
with open(os.path.join(
        BASE_DIR, 'pokemontcg', 'secrets.json')) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exception.'''
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)




# Create your views here.
def showData(request):
    dbname = get_secret("database_name")
    user = get_secret("database_user")
    host = get_secret("database_host")
    port = get_secret("database_port")
    password = get_secret("database_pwd")
    
    connectString = 'dbname=\'{db_name}\' user=\'{db_user}\' host=\'{db_host}\' port=\'{db_port}\' password=\'{db_password}\''.format(db_name=dbname, db_user=user, db_host=host, db_port=int(port), db_password=password)
    print(connectString)
    # Use variables to load df from database
    engine = pg.connect(connectString)
    df_pokemon = pd.read_sql('select * from pokedex_pokemon', con=engine)
    df_trainer = pd.read_sql('select * from pokedex_trainer', con=engine)
    df_energy = pd.read_sql('select * from pokedex_energy', con=engine)
    
    ### Pie Charts ###
    
    # Supertypes
    sizes = [len(df_pokemon.index), len(df_trainer.index), len(df_energy.index)]
    labels = ['Pokemon', 'Trainers', 'Energy']
    colors = ['#dd93ac', '#94e0e8', '#f8c471']
    fig1, ax1 = plt.subplots(figsize=(6, 6))
    ax1.pie(sizes, labels=labels, autopct='%1.0f%%', colors=colors)
    plt.title('Percentage of cards based on supertype')

    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri1 = urllib.parse.quote(string)
    
    # Types
    df_pokemon_types_link = pd.read_sql('select * from pokedex_pokemon_types', con=engine).set_index('pokemon_id').drop(['id'], axis=1)
    df_types = pd.read_sql('select * from pokedex_type', con=engine)
    df_pokemon_types = pd.merge(df_pokemon, df_pokemon_types_link, left_on='id', right_on='pokemon_id')
    df_pokemon_types = pd.merge(df_pokemon_types, df_types, left_on='type_id', right_on='id', suffixes=[None, '_type']).drop(['id_type'], axis=1)
    df_type_count = df_pokemon_types.groupby(['name_type'], as_index=False).count()
    df_type_count
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    labels = df_type_count['name_type']
    # colors = ['#8f8f8f', '#96795a', '#e6975c', '#338039', '#f5e662', '#9265a8', '#5581d4']
    ax2.pie(df_type_count['id'], autopct='%1.0f%%', labels=labels)
    plt.title('Percentage of cards based on type')

    buf = io.BytesIO()
    fig2.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri2 = urllib.parse.quote(string)
    
    # Rarity
    df_rarity = df_pokemon.groupby(['rarity'], as_index=False).count()
    fig3, ax3 = plt.subplots(figsize=(6, 6))
    labels = df_rarity['rarity']
    # colors = ['#8c8c8c', '#5399cf', '#d9b92b', '#41a363']
    ax3.pie(df_rarity['id'], autopct='%1.0f%%', labels=labels, labeldistance=1.2)
    plt.title('Percentage of cards based on rarity')

    buf = io.BytesIO()
    fig3.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri3 = urllib.parse.quote(string)
    
    ### Bar Charts ###
    
    # Supertypes
    Pokemon = len(df_pokemon.index)
    Trainer = len(df_trainer.index)
    Energy = len(df_energy.index)

    sizes = [Pokemon, Trainer, Energy]
    names = ['Pokemon','Trainer', 'Energy']
    colors = ['#dd93ac', '#94e0e8', '#f8c471']
    fig4, ax4 = plt.subplots(figsize=(16, 6))
    ax4.bar(names, sizes, color=colors)
    plt.title('Number of Pokemon Cards')
    plt.xlabel('Type of Card')
    plt.ylabel('Number of Cards')
    buf = io.BytesIO()
    fig4.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri4 = urllib.parse.quote(string)
    
    # Types
    df_pokemon_types_link = pd.read_sql('select * from pokedex_pokemon_types', con=engine).set_index('pokemon_id').drop(['id'], axis=1)
    df_types = pd.read_sql('select * from pokedex_type', con=engine)
    df_pokemon_types = pd.merge(df_pokemon, df_pokemon_types_link, left_on='id', right_on='pokemon_id')
    df_pokemon_types = pd.merge(df_pokemon_types, df_types, left_on='type_id', right_on='id', suffixes=[None, '_type']).drop(['id_type'], axis=1)
    df_type_count = df_pokemon_types.groupby(['name_type'], as_index=False).count()
    df_type_count
    fig5, ax5 = plt.subplots(figsize=(16, 6))
    labels = df_type_count['name_type']
    # colors = ['#8f8f8f', '#96795a', '#e6975c', '#338039', '#f5e662', '#9265a8', '#5581d4']

    ax5.bar(labels, df_type_count['id'])
    plt.title('Number of Cards of Each Type')
    plt.xlabel('Types')
    plt.ylabel('Number of Cards')
    buf = io.BytesIO()
    fig5.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri5 = urllib.parse.quote(string)
    
    # Rarity
    pokemon_r = (df_pokemon.groupby('rarity').size())
    trainer_r = (df_trainer.groupby('rarity').size())

    trainer_r = trainer_r.reindex(pokemon_r.index, fill_value=0)
    result = pokemon_r + trainer_r
    # colors = ['#8c8c8c', '#5399cf', '#d9b92b', '#41a363']
    # rarities = ['Common', 'Rare', 'Rare Holo', 'Uncommon']
    df_rarity = df_pokemon.groupby(['rarity'], as_index=False).count()
    rarities = df_rarity['rarity']
    fig6, ax6 = plt.subplots(figsize=(16, 6))
    ax6.bar(rarities, result)
    plt.title('Number of Cards in Each Rarity')
    plt.xlabel('Rarities')
    plt.ylabel('Number of Cards')
    buf = io.BytesIO()
    fig6.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri6 = urllib.parse.quote(string)
    
    return render(request, 'cardData/showData.html', {'piesuper': uri1, 'pietypes': uri2, 'pierarity': uri3, 'barsuper': uri4, 'bartypes': uri5, 'barrarity': uri6})
