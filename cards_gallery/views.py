from django.shortcuts import render
from .models import *
from random import sample, choice



def home(request):
    categories = Card.objects.filter(is_category=True)
    print(categories)
    context = {"categories": categories}
    return render(request, "cards_gallery/index.html", context)


def category_page(request, slug):
    #slug = slug.split('/')[-1]
    #print(slug)
    category = Card.objects.get(slug=slug)
    print(category)
    cards = category.cards.all()

    context = {"category": category, "cards": cards}
    return render(request, "cards_gallery/category.html", context)




def game_page(request, game_num, slug):
    NUM_CARDS = 10
    game_num = str(game_num)
    num_visits = request.session.get(game_num + '_num_visits', 0)
    print(num_visits)
    #request.session[game_num + '_num_visits'] = num_visits + 1

    category = Card.objects.get(slug=slug)
    pks = category.cards.values_list('slug', flat=True)
    random_pk = sample(list(pks), 4)
    cards = category.cards.filter(slug__in=random_pk)

    answer = choice(cards)  # It seems without choice, it takes first images in DB more often

    context = {"game_num": game_num, "slug": slug, "answer": answer, "cards": cards,
               "progress_width": 100 * num_visits / NUM_CARDS, "next_progress": 100 * (num_visits + 1) / NUM_CARDS}
    return render(request, "games/game_where_is.html", context)


def test(request):
    return render(request, "test.html")
