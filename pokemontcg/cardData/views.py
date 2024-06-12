from django.shortcuts import render, redirect
import os
import json

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
    
    return render(request, 'cardData/showData.html')
