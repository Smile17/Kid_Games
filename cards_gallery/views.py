from django.shortcuts import render
from .models import *


def home(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "index.html", context)


def categoryPage(request, slug):
    category = Category.objects.get(slug=slug)
    cards = category.cards.all()

    context = {"category": category, "cards": cards}
    return render(request, "category.html", context)


def test(request):
    return render(request, "test.html")
