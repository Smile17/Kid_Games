from django.shortcuts import render
from .models import *
from random import sample, choice
from cards_gallery.models import Card

games = {
    0: "cards_games/game_where_is.html",
    1: "cards_games/game_where_is_sound.html",
}


def game_page(request, game_num, slug):
    if request.method == "POST":
        print("AAAAAAAAAAAAAA")
        data = request.POST.get('num_visits')
        print(data)
    print("BBBBB")
    # Choose the game
    game_key, template_path = choice(list(games.items()))

    category = Card.objects.get(slug=slug)
    pks = category.cards.values_list('slug', flat=True)
    random_pk = sample(list(pks), 4)
    cards = category.cards.filter(slug__in=random_pk)
    answer = choice(cards)  # It seems without choice it takes first images in DB more often

    context = {"game_num": game_num, "slug": slug, "answer": answer, "cards": cards}
    return render(request, template_path, context)


