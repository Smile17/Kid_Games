from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.user_settings, name="user_settings"),
    path("application_settings", views.application_settings, name="application_settings"),
    path("change_password", views.change_password, name="change_password"),
    path("user_edit", views.user_edit, name="user_edit"),
]


