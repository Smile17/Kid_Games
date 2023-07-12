from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("test", views.test, name="test"),
    path("game/<int:game_num>/<slug:slug>", views.game_page, name="image-game"),
    path("<slug:slug>", views.category_page, name="image-category"),
]
