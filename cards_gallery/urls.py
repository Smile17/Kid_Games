from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("test", views.test, name="test"),
    path("save_tags", views.crud_tags, name="save_tags"),
    path("delete_tags", views.crud_tags, name="delete_tags"),
    path("<slug:slug>", views.category_page, name="image-category"),

]
