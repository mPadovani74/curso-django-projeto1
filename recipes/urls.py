
from django.urls import path, include
from django.contrib import admin
from recipes.views import home, contato, sobre


# dominio/recipes/
urlpatterns = [
    path('sobre/', sobre), # /sobre/
    path('home/', sobre), # /sobre/
    path('', home), # Home
    path('contato/', contato), # /contato/
]
