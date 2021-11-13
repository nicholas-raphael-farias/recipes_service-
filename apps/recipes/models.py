"""
Models for recipes app
    Recipe:
    Ingredient:
"""

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import CharField
from core.models import Dates


class Recipe(Dates):
    """..."""
    name = models.CharField(max_length=50, unique=True, help_text="recipe's name")
    ingredients  = ArrayField(base_field=CharField(max_length=50, help_text="recipe's ingredient"))


class Ingredient(Dates):
    """..."""
    name = models.CharField(max_length=50, unique=True, help_text="ingredient's name")
    recipes  = ArrayField(base_field=CharField(max_length=50, help_text="recipes where the ingredient is used"))