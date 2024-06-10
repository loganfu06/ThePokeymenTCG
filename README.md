# ThePokeymenTCG

## Roster
- Logan Fu: Project manager, add card and search for card functionality.
- Jonathan Yap: Detail views for trainers and energy, bar graphs, and price comparison.
- Marcus Negron: Home page/nav bar, user authentication, detail view for Pokemon, pie graphs.
- Calvin Pun: List views, bar graphs.

## Summary
The purpose of this website is to search, retrieve, store, and display Pokemon card data. Detailed information about the apps is on the home page,
inserting and displaying Pokemon card data is on the Pokedex app, and general information/data about card data in your database, and the price comparison function, is in the CardData app.

## API Used
https://pokemontcg.io/

## Launch Codes
1. Make pyenv in the Project repo:
- pyenv local 3.11.5
- python -m venv env_3.11.5
2. Install packages with pip install:
- pip install --upgrade pip-tools pip setuptools wheel
- pip-compile --upgrade --generate-hashes --output-file requirements_env/main.txt requirements_env/main.in
- pip-compile --upgrade --generate-hashes --output-file requirements_env/dev.txt requirements_env/dev.in
- pip-sync requirements_env/main.txt requirements_env/dev.txt
3. Make a nodeenv:
- pip install nodeenv
- nodeenv --node=20.11.1 --prebuilt env_node_20.11.1
- Deactivate the pyenv
- Activate the node env and go to ../ThePokeymenTCG/pokemontcg_vue
- Run npm install
- Run npm run dev
4. Go to ../ThePokeymen/pokemon/pokemon and make a secrets.json file
- Follow the format in secrets_template.json
5. In a new terminal, go to ../ThePokeymenTCG
- Activate the pyenv
6. Go to ../ThePokeymenTCG/pokemon
- Run python manage.py makemigrations
- Run python manage.py migrate
- Run python manage.py runserver
7. Go to 127.0.0.1:8000/pokedex
- Load initial data using the initial data button (this may take some time)
- The app is now ready to use!

How to enter new Pokemon into the database:
- In the Pokedex app, type a Pokemon name, or a part of a Pokemon's name, into the search bar on the Pokedex app. Then select the Pokemon from the dropdown, and press the "Add to Pokedex" button.

How to battle two Pokemon:
- In the Type app, select two Pokemon from the existing database, then press the "Battle Pokemon" button.
