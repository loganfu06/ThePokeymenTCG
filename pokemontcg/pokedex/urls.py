from django.urls import path

from . import views

app_name = "pokedex"

urlpatterns = [
    path("search", views.testView, name="search"),
    path("pokemon_list", views.PokemonListView.as_view(), name="pokemon_list"),
    path("trainer_list", views.TrainerListView.as_view(), name="trainer_list"),
    path("energy_list", views.EnergyListView.as_view(), name="energy_list"),
    path("test", views.testView, name="test"),
    path("loadInitialData", views.loadInitialData, name="loadInitialData"),
    path("create/<str:card_id>", views.createPokemonCard, name="create"),
    path("search/<str:card_name>", views.searchView, name="search")
    path("", views.homeView, name='home'),
    path("bis/<int:pk>", views.PokemonDetailbisView.as_view(), name="pokemon_detail_bis",),
    path( "js/<int:pk>", views.PokemonDetailJsView.as_view(), name="pokemon_detail_js", ),
]