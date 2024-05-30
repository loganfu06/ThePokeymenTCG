from django.urls import path

from . import views

app_name = "pokedex"

urlpatterns = [
    path("test", views.testView, name="test"),
    path("loadInitialData", views.loadInitialData, name="loadInitialData"),
    path("create/<str:card_id>", views.createPokemonCard, name="create"),
    path("search", views.searchView, name="search")
]