from django.urls import path, re_path
from . import views


urlpatterns = [
    path("<int:game_num>/<slug:slug>", views.game_page, name="image-game"),
]


