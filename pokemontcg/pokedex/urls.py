from django.urls import path

from . import views

app_name = "pokedex"

urlpatterns = [
    path("", views.PokemonListView.as_view(), name="pokemon_list"),
    path("test", views.testView, name="test"),
    path("loadInitialData", views.loadInitialData, name="loadInitialData"),
    path("create/<str:card_id>", views.createPokemonCard, name="create")
]