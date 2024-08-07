
from django.urls import path, include

from recipes.views import home


# dominio/recipes/
urlpatterns = [
    path('', home), # Home
]
