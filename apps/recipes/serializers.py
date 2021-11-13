from rest_framework import serializers
from .models import (Recipe, Ingredient)


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for Recipe model
    """
    class Meta:
        model = Recipe
        fields = ('name', 'ingredients')
        

class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for Recipe model
    """
    class Meta:
        model = Ingredient
        fields = ('name', 'recipes')