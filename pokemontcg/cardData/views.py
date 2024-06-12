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
    
    # Use variables to load df from database
    engine = pg.connect("dbname='postgres' user='postgres' host='127.0.0.1' port='5432' password='4$g@38XUa2MvFb'")
    df_pokemon = pd.read_sql('select * from pokedex_pokemon', con=engine)
    df_trainer = pd.read_sql('select * from pokedex_trainer', con=engine)
    df_energy = pd.read_sql('select * from pokedex_energy', con=engine)
    
    # Supertypes
    sizes = [len(df_pokemon.index), len(df_trainer.index), len(df_energy.index)]
    labels = ['Pokemon', 'Trainers', 'Energy']
    colors = ['#dd93ac', '#94e0e8', '#f8c471']
    fig1, ax1 = plt.subplots(figsize=(6, 6))
    ax1.pie(sizes, labels=labels, autopct='%1.0f%%', colors=colors)
    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    
    
    return render(request, 'cardData/showData.html', {'data': uri})
