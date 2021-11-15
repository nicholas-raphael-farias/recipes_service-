# recipes_service-
Simple service to handle recipes and ingredients

# Recipes service REST API 

This is a simple rest api to handle recipes and and ingredients,
The service is using Django and REST Framework libraries 


## Requirements 
 
## Local development
 cd local
 sudo docker-compose -p recipes_service up
### Run db migrations 
 sudo docker-compose -p recipes_service exec recipes_api python manage.py migrate 

# Services 
The different endpoints available are described below.

## Get list of recipes

### Request

`GET /api/v1/recipes/`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/recipes 

## Search a recipe by name 

### Request 

`GET /api/v1/recipes/?search=[_recipe_name_]

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/recipes?search=[_recipe_name_]

## Search an ingredient 
 The endpoint shows all the recipes that contain a certain ingredient 



