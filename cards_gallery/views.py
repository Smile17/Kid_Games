from django.shortcuts import render
from .models import *
from random import sample



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




def game_page(request, slug):
    category = Card.objects.get(slug=slug)
    #cards = category.cards.all()[:4]
    pks = category.cards.values_list('slug', flat=True)
    random_pk = sample(list(pks), 4)
    cards = category.cards.filter(slug__in=random_pk)

    answer = cards[0]

    context = {"slug": slug, "answer": answer, "cards": cards}
    return render(request, "games/game_where_is.html", context)


def test(request):
    return render(request, "test.html")
