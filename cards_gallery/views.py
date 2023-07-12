from django.shortcuts import render
from .models import *
from random import sample, choice


def home(request):
    categories = Card.objects.filter(is_category=True)
    print(categories)
    context = {"categories": categories}
    return render(request, "cards_gallery/index.html", context)


def category_page(request, slug):
    category = Card.objects.get(slug=slug)
    print(category)
    cards = category.cards.all()

    context = {"category": category, "cards": cards}
    return render(request, "cards_gallery/category.html", context)


games = {
    0: "games/game_where_is.html",
    1: "games/game_where_is_sound.html",
}


def game_page(request, game_num, slug):
    # Choose the game
    game_key, template_path = choice(list(games.items()))

    category = Card.objects.get(slug=slug)
    pks = category.cards.values_list('slug', flat=True)
    random_pk = sample(list(pks), 4)
    cards = category.cards.filter(slug__in=random_pk)
    answer = choice(cards)  # It seems without choice it takes first images in DB more often

    context = {"game_num": game_num, "slug": slug, "answer": answer, "cards": cards}
    return render(request, template_path, context)


def test(request):
    return render(request, "test.html")
