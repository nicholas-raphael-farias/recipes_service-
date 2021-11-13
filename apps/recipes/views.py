from rest_framework import mixins, viewsets
from rest_framework.response import Response
from .serializers import (RecipeSerializer, IngredientSerializer)
from .models import (Recipe, Ingredient)

class RecipesView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """..."""
    def get_queryset(self, search):
        if not search:
            recipes = Recipe.objects.all()
        else:
            recipes = Recipe.objects.filter(name__contains=search)
        return recipes

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        search = request.GET.get('search', None)
        queryset = self.get_queryset(search)
        serializer = RecipeSerializer(queryset, many=True)
        return Response(serializer.data)


class IngredientsView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """..."""
    serializer_class = IngredientSerializer
    def get_queryset(self):
        return Ingredient.objects.all()