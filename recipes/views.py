
from django.http import HttpResponse
from django.shortcuts import render

from utils.recipes.factory import make_recipe

from .models import Recipe

# Create your views here.


def home(request):
    # return http request
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', status=200, context={'recipes': recipes})


def recipe(request, id):
    recipe = Recipe.objects.filter(id=id, is_published=True).first()
    return render(request, 'recipes/pages/recipe-view.html', status=200, context={'recipe': recipe, 'is_detail_page': True})


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/category.html', status=200, context={'recipes': recipes})
