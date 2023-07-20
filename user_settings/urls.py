from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.user_settings, name="user_settings"),
    path("application_settings", views.application_settings, name="application_settings"),
]


