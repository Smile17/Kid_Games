from django.shortcuts import render
from .models import *
from cards_gallery.models import Card


def scavenger_home(request):
    categories = ScavengerCard.objects.all()
    categories = [c.card for c in categories]
    context = {"categories": categories}
    return render(request, "scavenger_hunt/index.html", context)


def scavenger_category_page(request, slug):
    category = Card.objects.get(slug=slug)
    cards = category.cards.all()

    context = {"category": category, "cards": cards}
    return render(request, "scavenger_hunt/category.html", context)
