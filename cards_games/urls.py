from django.urls import path
from . import views


urlpatterns = [
    path("not_enough", views.not_enough, name="image_not_enough"),
    path("<int:game_num>/<slug:slug>", views.game_page, name="image_game"),
]


