from rest_framework.routers import SimpleRouter
from .views import RecipesView

RECIPES_ROUTER = SimpleRouter()

RECIPES_ROUTER.register(r'/recipes', RecipesView, 'recipes')