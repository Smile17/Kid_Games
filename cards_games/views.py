from django.shortcuts import render
from .models import *
from random import sample, choice
from user_settings.utils import get_user_settings
from cards_gallery.models import Card

games = {
    0: "cards_games/game_where_is.html",
    1: "cards_games/game_where_is_sound.html",
}


def game_page(request, game_num, slug):
    settings = {
        "num_question": request.GET.get('num_question', 10)
    }
    num = int(request.GET.get('num', 1))

    # Choose the game
    game_key, template_path = choice(list(games.items()))

    category = Card.objects.get(slug=slug)
    pks = category.cards.values_list('slug', flat=True)
    random_pk = sample(list(pks), 4)
    cards = category.cards.filter(slug__in=random_pk)
    answer = choice(cards)  # It seems without choice it takes first images in DB more often

    context = {"game_num": game_num, "slug": slug, "answer": answer, "cards": cards, "settings": settings, "next_num": num + 1}
    return render(request, template_path, context)

def not_enough(request):
    title = request.GET['title']
    context = {"title": title}
    return render(request, "cards_games/not_enough_error.html", context)
