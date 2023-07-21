from django.db.models import Exists, OuterRef
from django.shortcuts import render
from .models import *
from random import sample, choice
from user_settings.utils import get_user_settings


def home(request):
    categories = filter_cards(request, Card.objects, True)
    context = {"categories": categories}
    return render(request, "cards_gallery/index.html", context)

def filter_cards(request, cards_obj, is_category):
    is_filtered = False
    if request.user.is_authenticated:  # use personal tags if present, ignore global tags
        tags = request.GET.get('ptag', None)
        if not (tags is None):
            tags = tags.split(',')  # get categories with at least one of the selected tags
            cards = cards_obj.filter(
                Exists(CardTag.objects.filter(user=request.user, tag__in=tags, card=OuterRef('pk'))),
                is_category=is_category
            )
            is_filtered = True
    if not (is_filtered):  # filter on global filtering
        tags = request.GET.get('tag', None)
        if tags is None:
            cards = cards_obj.filter(is_category=is_category)
        else:
            tags = tags.split(',')  # get categories with at least one of the selected tags
            cards = cards_obj.filter(
                Exists(CardTag.objects.filter(user__isnull=True, tag__in=tags, card=OuterRef('pk'))),
                is_category=True
            )
    return cards

def category_page(request, slug):
    settings = get_user_settings(request)
    category = Card.objects.get(slug=slug)
    cards = filter_cards(request, category.cards, False)
    context = {"category": category, "cards": cards, "settings": settings}
    return render(request, "cards_gallery/category.html", context)



def test(request):
    return render(request, "test.html")
