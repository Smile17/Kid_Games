from django.shortcuts import render
from random import sample, choice
from cards_gallery.models import Card
from cards_gallery.views import filter_cards
from cards_games.models import GameType
from user_settings.models import UserSetting

games_keys = ["Find image by sound", "Find sound by image", "Paint text"]

def get_random_question(request):
    if request.user.is_authenticated:
        settings = UserSetting.objects.get(user=request.user)
        game_types = settings.games.values_list('title', 'template_name')
    else:
        game_types = GameType.objects.values_list('title', 'template_name')
    type = choice(game_types)
    return type

def game_page(request, game_num, slug):
    settings = {
        "num_question": request.GET.get('num_question', 10)
    }
    num = int(request.GET.get('num', 1))

    # Choose the game
    type = get_random_question(request)
    print(type)
    game_key, template_path = type[0], type[1]
    if game_key == games_keys[0] or game_key == games_keys[1]:
        category = Card.objects.get(slug=slug)
        cards = filter_cards(request, category.cards, False)
        pks = cards.values_list('slug', flat=True)
        random_pk = sample(list(pks), 4)
        cards = cards.filter(slug__in=random_pk)
        answer = choice(cards)  # It seems without choice it takes first images in DB more often

        context = {"game_num": game_num, "slug": slug, "answer": answer, "cards": cards, "settings": settings, "next_num": num + 1}
    elif game_key == games_keys[2]:
        category = Card.objects.get(slug=slug)
        cards = filter_cards(request, category.cards, False).filter(title__length__lt=6)
        answer = cards.order_by('?').first()
        context = {"game_num": game_num, "slug": slug, "answer": answer, "settings": settings,
                   "next_num": num + 1}

    return render(request, template_path, context)

def not_enough(request):
    title = request.GET['title']
    context = {"title": title}
    return render(request, "cards_games/not_enough_error.html", context)


