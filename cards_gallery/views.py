from django.db.models import Exists, OuterRef
from django.shortcuts import render
from .models import *
from random import sample, choice
from user_settings.utils import get_user_settings


def home(request):
    categories = filter_cards(request, Card.objects, True)
    tags = CardTag.objects.filter(user__isnull=True).values_list('tag', flat=True).distinct()
    ptags = []
    if request.user.is_authenticated:
        ptags = CardTag.objects.filter(user=request.user).values_list('tag', flat=True).distinct()
    context = {"categories": categories, "tags": tags, "ptags": ptags}
    return render(request, "cards_gallery/index.html", context)

def filter_cards(request, cards_obj, is_category):
    is_filtered = False
    if request.user.is_authenticated:  # use personal tags if present, ignore global tags
        tags = request.GET.get('ptag', None)
        if not (tags is None or len(tags) == 0):
            tags = tags.split(',')  # get categories with at least one of the selected tags
            cards = cards_obj.filter(
                Exists(CardTag.objects.filter(user=request.user, tag__in=tags, card_fk=OuterRef('pk'))),
                is_category=is_category
            )
            is_filtered = True
    if not (is_filtered):  # filter on global filtering
        tags = request.GET.get('tag', None)
        if not (tags is None or len(tags) == 0):
            tags = tags.split(',')  # get categories with at least one of the selected tags
            cards = cards_obj.filter(
                Exists(CardTag.objects.filter(user__isnull=True, tag__in=tags, card_fk=OuterRef('pk'))),
                is_category=True
            )
        else:
            cards = cards_obj.filter(is_category=is_category)
    return cards


def category_page(request, slug):
    settings = get_user_settings(request)
    category = Card.objects.get(slug=slug)
    cards = filter_cards(request, category.cards, False)
    context = {"category": category, "cards": cards, "settings": settings}
    return render(request, "cards_gallery/category.html", context)



def test(request):
    return render(request, "test.html")
