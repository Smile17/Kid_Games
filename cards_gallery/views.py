from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from user_settings.utils import get_user_settings
from django.contrib.auth.decorators import login_required

def home(request):
    categories = filter_cards(request, Card.objects, True)
    context = {"categories": categories}
    return render(request, "cards_gallery/index_game.html", context)


def category_page(request, slug):
    settings = get_user_settings(request)
    category = Card.objects.get(slug=slug)
    cards = filter_cards(request, category.cards, False)
    context = {"category": category, "cards": cards, "settings": settings}
    return render(request, "cards_gallery/category_game.html", context)


def home_with_tags(request):
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
            cards = cards_obj.filter(is_category=is_category, tags__tag__in=tags, tags__user=request.user)
            is_filtered = True
    if not (is_filtered):  # filter on global filtering
        tags = request.GET.get('tag', None)
        if not (tags is None or len(tags) == 0):
            tags = tags.split(',')  # get categories with at least one of the selected tags
            cards = cards_obj.filter(is_category=is_category, tags__tag__in=tags, tags__user__isnull=True)
        else:
            cards = cards_obj.filter(is_category=is_category)
    return cards


def category_page_with_tags(request, slug):
    settings = get_user_settings(request)
    category = Card.objects.get(slug=slug)
    cards = filter_cards(request, category.cards, False)
    tags = CardTag.objects.filter(user__isnull=True).values_list('tag', flat=True).distinct()
    ptags = []
    if request.user.is_authenticated:
        ptags = CardTag.objects.filter(user=request.user).values_list('tag', flat=True).distinct()
    context = {"category": category, "cards": cards, "settings": settings, "tags": tags, "ptags": ptags}
    return render(request, "cards_gallery/category.html", context)


#@login_required
def crud_tags(request):
    if request.method == 'POST' and 'HTTP_X_METHOD_OVERRIDE' in request.META:
        http_method = request.META['HTTP_X_METHOD_OVERRIDE']
        if http_method.lower() == 'delete':
            slug = request.POST["slug"]
            tag = request.POST["tag"]
            is_populate = request.POST["is_populate"]
            card = Card.objects.get(slug=slug)
            tag_obj = delete_tags(request, card, tag)
            if is_populate == "true":
                cards = card.cards.all()
                for card in cards:
                    card.tags.remove(tag_obj.id)
                    card.save()
            print("TAGS DELETED")
    elif request.method == 'POST':
        slug = request.POST["slug"]
        tags = request.POST["tags"].split(';')
        is_populate = request.POST["is_populate"]
        card = Card.objects.get(slug=slug)
        print(card)
        print(is_populate)
        tags_obj = save_tags(request, card, tags)
        if is_populate == "true":
            cards = card.cards.all()
            for card in cards:
                for tag_obj in tags_obj:
                    card.tags.add(tag_obj)
        print("TAGS ADDED")
    return HttpResponse("1")

def delete_tags(request, card, tag):
    tag_obj = card.tags.filter(tag=tag, user=request.user).get()
    card.tags.remove(tag_obj)
    card.save()
    return tag_obj
def save_tags(request, card, tags):
    tags_obj = []
    for tag in tags:
        tag_obj, created = CardTag.objects.get_or_create(tag=tag, user=request.user)
        tags_obj.append(tag_obj)
        card.tags.add(tag_obj)
    card.save()
    return tags_obj


def bad_request(request, exception):
    return redirect(reverse('home'))

