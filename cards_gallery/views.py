from django.shortcuts import render
from .models import *
from random import sample, choice


def home(request):
    categories = Card.objects.filter(is_category=True)
    context = {"categories": categories}
    return render(request, "cards_gallery/index.html", context)


def category_page(request, slug):
    category = Card.objects.get(slug=slug)
    cards = category.cards.all()

    context = {"category": category, "cards": cards}
    return render(request, "cards_gallery/category.html", context)



def test(request):
    return render(request, "test.html")
