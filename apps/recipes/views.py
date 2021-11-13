from rest_framework import mixins, viewsets
from rest_framework.response import Response
from .serializers import (RecipeSerializer, IngredientSerializer)
from .models import (Recipe, Ingredient)

class RecipesView(mixins.ListModelMixin, viewsets.GenericViewSet):
    def get_queryset(self):
        recipes = Recipe.objects.all()
        return recipes

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = RecipeSerializer(queryset, many=True)
        return Response(serializer.data)