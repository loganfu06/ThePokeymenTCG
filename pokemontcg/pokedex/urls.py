from django.urls import path

from . import views

app_name = "pokedex"

urlpatterns = [
    path("list", views.PokemonListView.as_view(), name="pokemon_list"),
    path("test", views.testView, name="test"),
    path("loadInitialData", views.loadInitialData, name="loadInitialData"),
    path("create/<str:card_id>", views.createPokemonCard, name="create"),
    path("", views.homeView, name='home'),
    path("bis/<int:pk>", views.PokemonDetailbisView.as_view(), name="pokemon_detail_bis",),
    path( "js/<int:pk>", views.PokemonDetailJsView.as_view(), name="pokemon_detail_js", ),
]