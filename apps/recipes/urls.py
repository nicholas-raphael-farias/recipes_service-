from rest_framework.routers import SimpleRouter
from .views import (RecipesView, IngredientsView)

RECIPES_ROUTER = SimpleRouter()

RECIPES_ROUTER.register(r'/recipes', RecipesView, 'recipes')
RECIPES_ROUTER.register(r'/ingredients', IngredientsView, 'ingredients')