from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("edit", views.home_with_tags, name="home_with_tags"),
    path("edit/save_tags", views.crud_tags, name="save_tags"),
    path("edit/delete_tags", views.crud_tags, name="delete_tags"),
    path("edit/<slug:slug>", views.category_page_with_tags, name="image_category_with_tags"),
    path("<slug:slug>", views.category_page, name="image_category"),

]
