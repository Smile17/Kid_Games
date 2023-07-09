from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("test", views.test, name="test"),
    #re_path(r'[<slug:slug>/]+', views.category_page, name="image-category"),
    path("game/<slug:slug>", views.game_page, name="image-game"),
    path("<slug:slug>", views.category_page, name="image-category"),
]
