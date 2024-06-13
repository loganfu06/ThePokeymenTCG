from django.urls import path

from . import views

app_name = "cardData"

urlpatterns = [
    path("showData", views.showData, name="showData"),

]