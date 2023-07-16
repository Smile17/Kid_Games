from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.scavenger_home, name="scavenger-home"),
    path("<slug:slug>", views.scavenger_category_page, name="scavenger-category"),
]


