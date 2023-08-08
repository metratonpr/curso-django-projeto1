from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe

# Create your views here.


def home(request):
    # return http request41
    recipes = get_list_or_404(Recipe.objects.filter(
        is_published=True).order_by('-id'))
    return render(request, 'recipes/pages/home.html',
    context={'recipes': recipes})  # noqa


def recipe(request, id):
    recipe = get_object_or_404(Recipe.objects.filter(
        pk=id, is_published=True))

    return render(request, 'recipes/pages/recipe-view.html',
    context={'recipe': recipe, 'is_detail_page': True})  # noqa


def category(request, category_id):
    # recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    # if not recipes:
    #     raise Http404('Not Found')
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id'))
    return render(request, 'recipes/pages/category.html',
    context={'recipes': recipes, 'title': f'{recipes[0].category.name}  - Category | '})  # noqa
