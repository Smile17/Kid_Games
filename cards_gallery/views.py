from django.shortcuts import render
from .models import *


def home(request):
    categories = Card.objects.filter(is_category=True)
    print(categories)
    context = {"categories": categories}
    return render(request, "index.html", context)


def category_page(request, slug):
    #slug = slug.split('/')[-1]
    #print(slug)
    category = Card.objects.get(slug=slug)
    print(category)
    cards = category.cards.all()

    context = {"category": category, "cards": cards}
    return render(request, "category.html", context)

def game_page(request, slug):
    category = Card.objects.get(slug=slug)
    cards = category.cards.all()

    context = {"category": category, "cards": cards}
    return render(request, "game.html", context)


def test(request):
    return render(request, "test.html")
